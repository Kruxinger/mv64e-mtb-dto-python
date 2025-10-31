from mv64e_dto.clin_var_coding import ClinVarCoding
from mv64e_dto.clin_var_coding_code import ClinVarCodingCode

def test_clin_var_coding_initialization():
    c = ClinVarCoding(
        code=ClinVarCodingCode.CODE_2,
        display="Likely benign",
        system="http://www.ncbi.nlm.nih.gov/clinvar"
    )
    assert c.code == ClinVarCodingCode.CODE_2
    assert c.display == "Likely benign"
    # Prüft die Serialisierung des Enums
    assert c.model_dump(by_alias=True)["code"] == "2"

def test_clin_var_coding_alias_input():
    data = {
        "code": "5",
        "version": "v1"
    }
    c = ClinVarCoding(**data)
    assert c.code == ClinVarCodingCode.CODE_5
    assert c.version == "v1"

def test_clin_var_coding_missing_optional_fields():
    c = ClinVarCoding(code=ClinVarCodingCode.CODE_4)
    assert c.display is None
    assert c.system is None
    assert c.model_dump()["display"] is None