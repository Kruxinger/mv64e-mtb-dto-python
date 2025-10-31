from datetime import date
from mv64e_dto.provision import Provision
from mv64e_dto.model_project_consent_purpose import ModelProjectConsentPurpose
from mv64e_dto.consent_provision import ConsentProvision  # Simuliert

# Dummy-Daten
DUMMY_TYPE = ConsentProvision(code="N", display="Nicht erforderlich")


def test_provision_initialization():
    provision_date = date(2025, 6, 1)
    p = Provision(
        date=provision_date,
        purpose=ModelProjectConsentPurpose.SEQUENCING,
        type=DUMMY_TYPE
    )
    assert p.date == provision_date
    assert p.purpose == ModelProjectConsentPurpose.SEQUENCING
    assert p.type.code == "N"


def test_provision_serialization_and_deserialization():
    data = {
        "date": "2024-11-20",
        "purpose": "reidentification",
        "type": {"code": "E", "display": "Erforderlich"}
    }
    p = Provision(**data)

    # Überprüfung der Deserialisierung
    assert p.date == date(2024, 11, 20)
    assert p.purpose == ModelProjectConsentPurpose.REIDENTIFICATION

    # Überprüfung der Serialisierung (Alias-Namen und Datumsformat)
    dump = p.model_dump(by_alias=True, mode='json')
    assert dump["date"] == "2024-11-20"
    assert dump["purpose"] == "reidentification"
    assert dump["type"]["code"] == "E"