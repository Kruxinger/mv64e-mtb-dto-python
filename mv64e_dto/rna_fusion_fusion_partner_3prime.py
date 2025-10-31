from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.coding import Coding
from mv64e_dto.rna_fusion_strand import RnaFusionStrand
from mv64e_dto.transcript_id import TranscriptId


class RnaFusionFusionPartner3Prime(BaseModel):
    exon_id: Optional[str] = Field(default=None, alias="exonId")
    gene: Optional[Coding] = Field(default=None, alias="gene") # PLACEHOLDER: Coding
    position: Optional[float] = Field(default=None, alias="position") # double in Java
    strand: Optional[RnaFusionStrand] = Field(default=None, alias="strand")
    transcript_id: Optional[TranscriptId] = Field(default=None, alias="transcriptId") # PLACEHOLDER: TranscriptId

    model_config = {"populate_by_name": True, "from_attributes": True}