from mv64e_dto.mvh_metadata import MvhMetadata
from mv64e_dto.mvh_submission_type import MvhSubmissionType

def test_mvh_metadata_deserialization():
    data = {
        "modelProjectConsent": {"status": "present"}, # Dummy
        "researchConsents": [
            {"type": "genetics", "status": "approved"},
            {"type": "clinical", "status": "pending"}
        ],
        "transferTAN": "1234-ABCD",
        "type": "initial"
    }
    metadata = MvhMetadata(**data)

    assert metadata.transfer_tan == "1234-ABCD"
    assert metadata.type == MvhSubmissionType.INITIAL
    assert metadata.model_project_consent["status"] == "present"
    assert len(metadata.research_consents) == 2
    assert metadata.research_consents[1]["type"] == "clinical"

def test_mvh_metadata_serialization():
    metadata = MvhMetadata(
        transfer_tan="5678-WXYZ",
        type=MvhSubmissionType.CORRECTION
    )
    dump = metadata.model_dump(by_alias=True, exclude_none=True)
    assert dump["transferTAN"] == "5678-WXYZ"
    assert dump["type"] == "correction"
    assert "researchConsents" not in dump