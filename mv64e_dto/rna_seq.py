from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.base_variant_localization_coding import BaseVariantLocalizationCoding
from mv64e_dto.coding import Coding
from mv64e_dto.reference import Reference
from mv64e_dto.transcript_id import TranscriptId
from mv64e_dto.variant_external_id import VariantExternalId



class RnaSeq(BaseModel):
    cohort_ranking: Optional[int] = Field(default=None, alias="cohortRanking") # Long in Java
    external_ids: Optional[List[VariantExternalId]] = Field(default=None, alias="externalIds") # PLACEHOLDER: List[VariantExternalId]
    gene: Optional[Coding] = Field(default=None, alias="gene") # PLACEHOLDER: Coding
    id: Optional[str] = Field(default=None, alias="id")
    library_size: Optional[int] = Field(default=None, alias="librarySize") # Long in Java
    localization: Optional[List[BaseVariantLocalizationCoding]] = Field(default=None, alias="localization") # PLACEHOLDER: List[BaseVariantLocalizationCoding]
    patient: Optional[Reference] = Field(default=None, alias="patient")
    raw_counts: Optional[int] = Field(default=None, alias="rawCounts") # long in Java
    tissue_corrected_expression: Optional[bool] = Field(default=None, alias="tissueCorrectedExpression")
    transcript_id: Optional[TranscriptId] = Field(default=None, alias="transcriptId")
    transcripts_per_million: Optional[float] = Field(default=None, alias="transcriptsPerMillion") # double in Java
    variant: Optional[Reference] = Field(default=None, alias="variant")

    model_config = {"populate_by_name": True, "from_attributes": True}