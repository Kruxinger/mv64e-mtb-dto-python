from typing import Optional, List
from pydantic import BaseModel, Field
from mv64e_dto.chromosome import Chromosome
from mv64e_dto.reference import Reference
from mv64e_dto.cnv_coding import CnvCoding
from mv64e_dto.coding import Coding
from mv64e_dto.end_range import EndRange
from mv64e_dto.start_range import StartRange
from mv64e_dto.variant_external_id import VariantExternalId
from mv64e_dto.base_variant_localization_coding import BaseVariantLocalizationCoding # Angenommen existiert

class Cnv(BaseModel):
    chromosome: Optional[Chromosome] = Field(
        default=None,
        alias="chromosome"
    )
    cn_a: Optional[float] = Field(
        default=None,
        alias="cnA"
    )
    cn_b: Optional[float] = Field(
        default=None,
        alias="cnB"
    )
    copy_number_neutral_lo_h: Optional[List[Coding]] = Field(
        default=None,
        alias="copyNumberNeutralLoH"
    )
    end_range: Optional[EndRange] = Field(
        default=None,
        alias="endRange"
    )
    external_ids: Optional[List[VariantExternalId]] = Field(
        default=None,
        alias="externalIds"
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
    relative_copy_number: Optional[float] = Field(
        default=None,
        alias="relativeCopyNumber"
    )
    reported_affected_genes: Optional[List[Coding]] = Field(
        default=None,
        alias="reportedAffectedGenes"
    )
    reported_focality: Optional[str] = Field(
        default=None,
        alias="reportedFocality"
    )
    start_range: Optional[StartRange] = Field(
        default=None,
        alias="startRange"
    )
    total_copy_number: Optional[int] = Field(
        default=None,
        alias="totalCopyNumber"
    )
    type: Optional[CnvCoding] = Field(
        default=None,
        alias="type"
    )

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }