from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

from mv64e_dto.brcaness import Brcaness
from mv64e_dto.cnv import Cnv
from mv64e_dto.dna_fusion import DnaFusion
from mv64e_dto.hrd_score import HrdScore
from mv64e_dto.rna_fusion import RnaFusion
from mv64e_dto.rna_seq import RnaSeq
from mv64e_dto.snv import Snv
from mv64e_dto.tmb import Tmb
from mv64e_dto.tumor_cell_content import TumorCellContent



class NgsReportResults(BaseModel):
    brcaness: Optional[Brcaness] = Field(default=None, alias="brcaness") # PLACEHOLDER: Brcaness
    copy_number_variants: Optional[List[Cnv]] = Field(default=None, alias="copyNumberVariants") # PLACEHOLDER: List[Cnv]
    dna_fusions: Optional[List[DnaFusion]] = Field(default=None, alias="dnaFusions") # PLACEHOLDER: List[DnaFusion]
    hrd_score: Optional[HrdScore] = Field(default=None, alias="hrdScore") # PLACEHOLDER: HrdScore
    rna_fusions: Optional[List[RnaFusion]] = Field(default=None, alias="rnaFusions") # PLACEHOLDER: List[RnaFusion]
    rna_seqs: Optional[List[RnaSeq]] = Field(default=None, alias="rnaSeqs") # PLACEHOLDER: List[RnaSeq]
    simple_variants: Optional[List[Snv]] = Field(default=None, alias="simpleVariants") # PLACEHOLDER: List[Snv]
    tmb: Optional[Tmb] = Field(default=None, alias="tmb") # PLACEHOLDER: Tmb
    tumor_cell_content: Optional[TumorCellContent] = Field(default=None, alias="tumorCellContent") # PLACEHOLDER: TumorCellContent

    model_config = {"populate_by_name": True, "from_attributes": True}