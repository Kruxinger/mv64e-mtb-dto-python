from pydantic import BaseModel
from mv64e_dto.study_system import StudySystem
from mv64e_dto.study_reference import StudyReference


# --- Tests für StudySystem ---

class SystemTestModel(BaseModel):
    system: StudySystem


def test_system_enum_values():
    assert StudySystem.DRKS.value == "DRKS"
    assert StudySystem.EUDRA_CT.value == "Eudra-CT"


def test_system_deserialization():
    model = SystemTestModel(system="NCT")
    assert model.system == StudySystem.NCT


# --- Tests für StudyReference ---

def test_study_reference_initialization():
    ref = StudyReference(
        id="NCT05000000",
        system=StudySystem.NCT,
        display="A Randomised Trial"
    )
    assert ref.id == "NCT05000000"
    assert ref.system == StudySystem.NCT


def test_study_reference_serialization_and_deserialization():
    data = {
        "id": "DRKS00028741",
        "system": "DRKS",
        "type": "PrimaryRegistration"
    }
    ref = StudyReference(**data)

    # Überprüfung der Deserialisierung
    assert ref.id == "DRKS00028741"
    assert ref.system == StudySystem.DRKS

    # Überprüfung der Serialisierung (Alias-Namen und Enum-Wert)
    dump = ref.model_dump(by_alias=True, exclude_none=True)
    assert dump["id"] == "DRKS00028741"
    assert dump["system"] == "DRKS"