from mv64e_dto.base_variant_localization_coding import BaseVariantLocalizationCoding
from mv64e_dto.base_variant_localization_coding_code import BaseVariantLocalizationCodingCode

def test_base_variant_localization_coding_initialization():
    b = BaseVariantLocalizationCoding(
        code=BaseVariantLocalizationCodingCode.CODING_REGION,
        display="Coding Region",
        system="GRCh38",
        version="v1"
    )
    assert b.code == BaseVariantLocalizationCodingCode.CODING_REGION
    assert b.display == "Coding Region"
    assert b.system == "GRCh38"
    assert b.version == "v1"

def test_base_variant_localization_coding_alias_input():
    data = {
        "code": "intronic",
        "display": "Intronic Region",
        "system": "GRCh37",
        "version": "v2"
    }
    b = BaseVariantLocalizationCoding(**data)
    assert b.code == BaseVariantLocalizationCodingCode.INTRONIC
    assert b.display == "Intronic Region"
    assert b.system == "GRCh37"
    assert b.version == "v2"
