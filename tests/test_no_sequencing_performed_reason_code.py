from mv64e_dto.no_sequencing_performed_reason_code import NoSequencingPerformedReasonCode

def test_no_sequencing_performed_reason_code_values():
    assert NoSequencingPerformedReasonCode.NON_GENETIC_CAUSE.value == "non-genetic-cause"
    assert NoSequencingPerformedReasonCode.NOT_RARE_DISEASE.value == "not-rare-disease"
    assert NoSequencingPerformedReasonCode.OTHER.value == "other"
    assert NoSequencingPerformedReasonCode.PSYCHOSOMATIC.value == "psychosomatic"
    assert NoSequencingPerformedReasonCode.TARGETED_DIAGNOSTICS_RECOMMENDED.value == "targeted-diagnostics-recommended"
