from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.base_variant_localization_coding import BaseVariantLocalizationCoding
from mv64e_dto.reference import Reference
from mv64e_dto.rna_fusion_fusion_partner_3prime import RnaFusionFusionPartner3Prime
from mv64e_dto.rna_fusion_fusion_partner_5prime import RnaFusionFusionPartner5Prime
from mv64e_dto.variant_external_id import VariantExternalId


class RnaFusion(BaseModel):
    effect: Optional[str] = Field(default=None, alias="effect")
    external_ids: Optional[List[VariantExternalId]] = Field(default=None, alias="externalIds") # PLACEHOLDER: List[VariantExternalId]
    fusion_partner_3prime: Optional[RnaFusionFusionPartner3Prime] = Field(default=None, alias="fusionPartner3prime")
    fusion_partner_5prime: Optional[RnaFusionFusionPartner5Prime] = Field(default=None, alias="fusionPartner5prime")
    id: Optional[str] = Field(default=None, alias="id")
    localization: Optional[List[BaseVariantLocalizationCoding]] = Field(default=None, alias="localization") # PLACEHOLDER: List[BaseVariantLocalizationCoding]
    patient: Optional[Reference] = Field(default=None, alias="patient")
    reported_num_reads: Optional[int] = Field(default=None, alias="reportedNumReads") # long in Java

    model_config = {"populate_by_name": True, "from_attributes": True}