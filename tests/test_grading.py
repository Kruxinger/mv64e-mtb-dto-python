from mv64e_dto.grading import Grading
from pydantic import BaseModel
from typing import Optional


# Simuliere das abhängige TumorGrading DTO für den Test
class TumorGrading(BaseModel):
    value: Optional[str] = None


DUMMY_GRADING_1 = TumorGrading(value="G1")
DUMMY_GRADING_2 = TumorGrading(value="G3")


def test_grading_initialization():
    g = Grading(history=[DUMMY_GRADING_1, DUMMY_GRADING_2])
    assert len(g.history) == 2
    assert g.history[0].value == "G1"


def test_grading_alias_input_and_serialization():
    data = {
        "history": [
            {"value": "G4"},
            {"value": "GX"}
        ]
    }
    g = Grading(**data)

    # Überprüfung der Deserialisierung
    assert g.history[1].value == "GX"

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = g.model_dump(by_alias=True)
    assert dump["history"][0]["value"] == "G4"