from mv64e_dto.care_plan_no_sequencing_performed_reason_coding import CarePlanNoSequencingPerformedReasonCoding
from mv64e_dto.no_sequencing_performed_reason_code import NoSequencingPerformedReasonCode

def test_care_plan_no_sequencing_performed_reason_coding_initialization():
    c = CarePlanNoSequencingPerformedReasonCoding(
        code=NoSequencingPerformedReasonCode.NON_GENETIC_CAUSE,
        display="Non-genetic Cause",
        system="GRCh38",
        version="v1"
    )
    assert c.code == NoSequencingPerformedReasonCode.NON_GENETIC_CAUSE
    assert c.display == "Non-genetic Cause"
    assert c.system == "GRCh38"
    assert c.version == "v1"

def test_care_plan_no_sequencing_performed_reason_coding_alias_input():
    data = {
        "code": "psychosomatic",
        "display": "Psychosomatic",
        "system": "GRCh37",
        "version": "v2"
    }
    c = CarePlanNoSequencingPerformedReasonCoding(**data)
    assert c.code == NoSequencingPerformedReasonCode.PSYCHOSOMATIC
    assert c.display == "Psychosomatic"
    assert c.system == "GRCh37"
    assert c.version == "v2"
