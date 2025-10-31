from mv64e_dto.base_variant_localization_coding_code import BaseVariantLocalizationCodingCode

def test_base_variant_localization_coding_code_values():
    assert BaseVariantLocalizationCodingCode.CODING_REGION.value == "coding-region"
    assert BaseVariantLocalizationCodingCode.INTERGENIC.value == "intergenic"
    assert BaseVariantLocalizationCodingCode.INTRONIC.value == "intronic"
    assert BaseVariantLocalizationCodingCode.REGULATORY_REGION.value == "regulatory-region"
    assert BaseVariantLocalizationCodingCode.SPLICING_REGION.value == "splicing-region"
