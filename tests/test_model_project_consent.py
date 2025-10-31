from datetime import datetime
from mv64e_dto.model_project_consent import ModelProjectConsent
from mv64e_dto.provision import Provision
from mv64e_dto.model_project_consent_purpose import ModelProjectConsentPurpose

# Dummy-Daten
DUMMY_PROVISIONS = [
    Provision(purpose=ModelProjectConsentPurpose.SEQUENCING, is_signed=True),
    Provision(purpose=ModelProjectConsentPurpose.REIDENTIFICATION, is_signed=False)
]


def test_mpc_initialization():
    consent_date = datetime(2025, 1, 15, 10, 30, 0)
    mpc = ModelProjectConsent(
        date=consent_date,
        provisions=DUMMY_PROVISIONS,
        version="1.0"
    )
    assert mpc.date == consent_date
    assert mpc.version == "1.0"
    assert len(mpc.provisions) == 2
    assert mpc.provisions[0].purpose == ModelProjectConsentPurpose.SEQUENCING


def test_mpc_serialization_and_deserialization():
    data = {
        "date": "2025-05-10T14:00:00",
        "version": "1.1",
        "provisions": [
            {"purpose": "case-identification", "isSigned": True}
        ]
    }
    mpc = ModelProjectConsent(**data)

    # Überprüfung der Deserialisierung (Datum und Enum)
    assert mpc.date.year == 2025
    assert mpc.provisions[0].purpose == ModelProjectConsentPurpose.CASE_IDENTIFICATION

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = mpc.model_dump(by_alias=True, mode='json')
    assert dump["version"] == "1.1"
    assert dump["provisions"][0]["purpose"] == "case-identification"
    # Pydantic verwendet standardmäßig ISO 8601 für datetime
    assert dump["date"] == "2025-05-10T14:00:00"