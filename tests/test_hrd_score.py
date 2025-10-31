from mv64e_dto.hrd_score import HrdScore
from mv64e_dto.components import Components
from mv64e_dto.reference import Reference
from mv64e_dto.hrd_score_interpretation_coding import HrdScoreInterpretationCoding
from pydantic import BaseModel, ValidationError
import pytest


# Simuliere InterpretationCodingCode Enum
class InterpretationCodingCode(str, BaseModel):
    POSITIVE = "positive"
    NEGATIVE = "negative"


DUMMY_COMPONENTS = Components(loh=0.5, lst=10.0, tai=8.0)
DUMMY_INTERPRETATION = HrdScoreInterpretationCoding(code=InterpretationCodingCode.POSITIVE, display="HRD-positive")
DUMMY_REF = Reference(id="ref_hrd")


def test_hrd_score_initialization():
    score = HrdScore(
        id="hrd_1",
        value=65.5,
        components=DUMMY_COMPONENTS,
        interpretation=DUMMY_INTERPRETATION,
        patient=DUMMY_REF
    )
    assert score.value == 65.5
    assert score.components.loh == 0.5
    assert score.interpretation.display == "HRD-positive"


def test_hrd_score_alias_input_and_serialization():
    data = {
        "id": "hrd_2",
        "value": 35.0,
        "components": {"loh": 0.1, "lst": 5.0, "tai": 2.5}
    }
    score = HrdScore(**data)

    # Überprüfung der Deserialisierung
    assert score.value == 35.0
    assert score.components.loh == 0.1

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = score.model_dump(by_alias=True)
    assert dump["value"] == 35.0
    assert dump["components"]["loh"] == 0.1


def test_hrd_score_missing_required_value():
    data = {"id": "hrd_c"}
    with pytest.raises(ValidationError):
        HrdScore(**data)