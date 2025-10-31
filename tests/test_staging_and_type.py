from datetime import date
from mv64e_dto.staging import Staging
from mv64e_dto.type import Type
from mv64e_dto.tumor_staging import TumorStaging
from mv64e_dto.tumor_staging_method_coding import TumorStagingMethodCoding
from mv64e_dto.tumor_staging_method_coding_code import TumorStagingMethodCodingCode
from mv64e_dto.coding import Coding

# Dummy-Daten
DUMMY_METHOD = TumorStagingMethodCoding(
    code=TumorStagingMethodCodingCode.PATHOLOGIC
)
DUMMY_OTHER_CODING = Coding(code="I", display="Immunohistochemistry")

def test_tumor_staging_deserialization():
    data = {
        "date": "2024-09-01",
        "method": {"code": "clinical"},
        "otherClassifications": [{"code": "AJCC-I"}]
        # tnmClassification fehlt
    }
    ts = TumorStaging(**data)
    assert ts.date == date(2024, 9, 1)
    assert ts.method.code == TumorStagingMethodCodingCode.CLINICAL
    assert ts.other_classifications[0].code == "AJCC-I"

def test_staging_deserialization_and_nesting():
    data = {
        "history": [
            {
                "date": "2023-01-01",
                "method": {"code": "pathologic"},
                "otherClassifications": [DUMMY_OTHER_CODING.model_dump()]
            }
        ]
    }
    staging = Staging(**data)
    assert len(staging.history) == 1
    assert staging.history[0].date == date(2023, 1, 1)
    assert staging.history[0].method.code == TumorStagingMethodCodingCode.PATHOLOGIC
    assert staging.history[0].other_classifications[0].code == "I"

def test_type_placeholder_handling():
    data = {
        "history": [
            {"typeCode": "primary"},  # Placeholder for History
            {"typeCode": "secondary"}
        ]
    }
    type_obj = Type(**data)
    assert len(type_obj.history) == 2
    assert type_obj.history[0]["typeCode"] == "primary"