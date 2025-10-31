from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.tumor_specimen_collection_localization_coding_code import TumorSpecimenCollectionLocalizationCodingCode

class LocalizationCodeTestModel(BaseModel):
    code: TumorSpecimenCollectionLocalizationCodingCode

def test_localization_code_values():
    assert TumorSpecimenCollectionLocalizationCodingCode.PRIMARY_TUMOR.value == "primary-tumor"
    assert TumorSpecimenCollectionLocalizationCodingCode.CELLFREE_DNA.name == "CELLFREE_DNA"

def test_localization_code_serialization():
    model = LocalizationCodeTestModel(code=TumorSpecimenCollectionLocalizationCodingCode.METASTASIS)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "metastasis"