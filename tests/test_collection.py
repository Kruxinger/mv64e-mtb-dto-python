from datetime import datetime
from mv64e_dto.collection import Collection
from mv64e_dto.tumor_specimen_collection_localization_coding import TumorSpecimenCollectionLocalizationCoding
from mv64e_dto.tumor_specimen_collection_localization_coding_code import TumorSpecimenCollectionLocalizationCodingCode
from mv64e_dto.tumor_specimen_collection_method_coding import TumorSpecimenCollectionMethodCoding
from mv64e_dto.tumor_specimen_collection_method_coding_code import TumorSpecimenCollectionMethodCodingCode

# Dummy-Daten
DUMMY_LOC = TumorSpecimenCollectionLocalizationCoding(code=TumorSpecimenCollectionLocalizationCodingCode.PRIMARY_TUMOR)
DUMMY_METHOD = TumorSpecimenCollectionMethodCoding(code=TumorSpecimenCollectionMethodCodingCode.BIOPSY)


def test_collection_initialization():
    dt = datetime(2025, 12, 10, 15, 30, 0)
    c = Collection(
        date=dt,
        localization=DUMMY_LOC,
        method=DUMMY_METHOD
    )
    assert c.date == dt
    assert c.localization.code == TumorSpecimenCollectionLocalizationCodingCode.PRIMARY_TUMOR
    assert c.method.code == TumorSpecimenCollectionMethodCodingCode.BIOPSY


def test_collection_alias_input_and_serialization():
    data = {
        "date": "2024-03-01T10:00:00Z",  # ISO 8601-String-Eingabe für datetime
        "localization": {"code": "metastasis"},
        "method": {"code": "resection"}
    }
    c = Collection(**data)

    # Überprüfung der Deserialisierung
    assert c.date == datetime(2024, 3, 1, 10, 0, 0)
    assert c.localization.code == TumorSpecimenCollectionLocalizationCodingCode.METASTASIS

    # Überprüfung der Serialisierung (Alias-Namen und ISO-Format)
    dump = c.model_dump(by_alias=True)
    assert dump["date"] == "2024-03-01T10:00:00Z"
    assert dump["localization"]["code"] == "metastasis"
    assert dump["method"]["code"] == "resection"