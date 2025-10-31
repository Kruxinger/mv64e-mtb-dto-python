from mv64e_dto.tumor_morphology import TumorMorphology
from mv64e_dto.reference import Reference
from mv64e_dto.coding import Coding

DUMMY_CODING = Coding(code="8000/3", display="Neoplasm, malignant")
DUMMY_REF_P = Reference(id="pat_m")


def test_tm_initialization():
    tm = TumorMorphology(
        id="tm_1",
        value=DUMMY_CODING,
        patient=DUMMY_REF_P,
        note="Small note."
    )
    assert tm.id == "tm_1"
    assert tm.value.code == "8000/3"
    assert tm.note == "Small note."


def test_tm_alias_input_and_serialization():
    data = {
        "id": "tm_2",
        "value": {"code": "8140/3", "system": "ICD-O-3"},
        "note": "Adenocarcinoma"
    }
    tm = TumorMorphology(**data)

    # Überprüfung der Deserialisierung
    assert tm.value.system == "ICD-O-3"

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = tm.model_dump(by_alias=True)
    assert dump["id"] == "tm_2"
    assert dump["value"]["code"] == "8140/3"