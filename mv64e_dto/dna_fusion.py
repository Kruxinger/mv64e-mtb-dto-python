from typing import Optional, List
from pydantic import BaseModel, Field
from mv64e_dto.reference import Reference
from mv64e_dto.variant_external_id import VariantExternalId
from mv64e_dto.dna_fusion_fusion_partner3_prime import DnaFusionFusionPartner3Prime
from mv64e_dto.dna_fusion_fusion_partner5_prime import DnaFusionFusionPartner5Prime
from mv64e_dto.base_variant_localization_coding import BaseVariantLocalizationCoding # Angenommen existiert

class DnaFusion(BaseModel):
    external_ids: Optional[List[VariantExternalId]] = Field(
        default=None,
        alias="externalIds"
    )
    fusion_partner3_prime: Optional[DnaFusionFusionPartner3Prime] = Field(
        default=None,
        alias="fusionPartner3prime"
    )
    fusion_partner5_prime: Optional[DnaFusionFusionPartner5Prime] = Field(
        default=None,
        alias="fusionPartner5prime"
    )
    id: Optional[str] = Field(
        default=None,
        alias="id"
    )
    localization: Optional[List[BaseVariantLocalizationCoding]] = Field(
        default=None,
        alias="localization"
    )
    patient: Optional[Reference] = Field(
        default=None,
        alias="patient"
    )
    # Java 'long' (primitiv) wird hier als required int angenommen
    reported_num_reads: int = Field(
        alias="reportedNumReads"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }