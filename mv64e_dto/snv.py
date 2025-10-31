from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.base_variant_localization_coding import BaseVariantLocalizationCoding
from mv64e_dto.chromosome import Chromosome
from mv64e_dto.clin_var_coding import ClinVarCoding
from mv64e_dto.coding import Coding
from mv64e_dto.position import Position
from mv64e_dto.reference import Reference
from mv64e_dto.transcript_id import TranscriptId
from mv64e_dto.variant_external_id import VariantExternalId



class Snv(BaseModel):
    allelic_frequency: Optional[float] = Field(default=None, alias="allelicFrequency") # double in Java
    alt_allele: Optional[str] = Field(default=None, alias="altAllele")
    chromosome: Optional[Chromosome] = Field(default=None, alias="chromosome") # PLACEHOLDER: Chromosome
    dna_change: Optional[str] = Field(default=None, alias="dnaChange")
    exon_id: Optional[str] = Field(default=None, alias="exonId")
    external_ids: Optional[List[VariantExternalId]] = Field(default=None, alias="externalIds") # PLACEHOLDER: List[VariantExternalId]
    gene: Optional[Coding] = Field(default=None, alias="gene") # PLACEHOLDER: Coding
    id: Optional[str] = Field(default=None, alias="id")
    interpretation: Optional[ClinVarCoding] = Field(default=None, alias="interpretation") # PLACEHOLDER: ClinVarCoding
    localization: Optional[List[BaseVariantLocalizationCoding]] = Field(default=None, alias="localization") # PLACEHOLDER: List[BaseVariantLocalizationCoding]
    patient: Optional[Reference] = Field(default=None, alias="patient")
    position: Optional[Position] = Field(default=None, alias="position") # PLACEHOLDER: Position
    protein_change: Optional[str] = Field(default=None, alias="proteinChange")
    read_depth: Optional[int] = Field(default=None, alias="readDepth") # long in Java
    ref_allele: Optional[str] = Field(default=None, alias="refAllele")
    transcript_id: Optional[TranscriptId] = Field(default=None, alias="transcriptId")

    model_config = {"populate_by_name": True, "from_attributes": True}