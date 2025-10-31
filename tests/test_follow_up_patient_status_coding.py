from mv64e_dto.follow_up_patient_status_coding import FollowUpPatientStatusCoding
from mv64e_dto.follow_up_patient_status_coding_code import FollowUpPatientStatusCodingCode

def test_status_coding_initialization():
    c = FollowUpPatientStatusCoding(
        code=FollowUpPatientStatusCodingCode.LOST_TO_FU,
        display="Lost to follow-up"
    )
    assert c.code == FollowUpPatientStatusCodingCode.LOST_TO_FU
    assert c.display == "Lost to follow-up"

def test_status_coding_alias_input():
    data = {
        "code": "lost-to-fu",
        "system": "http://system.org"
    }
    c = FollowUpPatientStatusCoding(**data)
    assert c.code == FollowUpPatientStatusCodingCode.LOST_TO_FU