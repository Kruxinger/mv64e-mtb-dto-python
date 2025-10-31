from mv64e_dto.dna_fusion_fusion_partner5_prime import DnaFusionFusionPartner5Prime
from mv64e_dto.chromosome import Chromosome
from mv64e_dto.coding import Coding
from pydantic import ValidationError
import pytest

DUMMY_GENE_CODING = Coding(code="GENE_5", display="Partner 5 Gene")

def test_partner5_prime_initialization():
    p5 = DnaFusionFusionPartner5Prime(
        chromosome=Chromosome.CHR1,
        gene=DUMMY_GENE_CODING,
        position=10000.0
    )
    assert p5.chromosome == Chromosome.CHR1
    assert p5.gene.code == "GENE_5"
    assert p5.position == 10000.0

def test_partner5_prime_missing_required_position():
    data = {"chromosome": "chr1"}
    with pytest.raises(ValidationError):
        DnaFusionFusionPartner5Prime(**data)