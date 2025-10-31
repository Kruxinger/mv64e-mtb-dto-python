from mv64e_dto.dna_fusion_fusion_partner3_prime import DnaFusionFusionPartner3Prime
from mv64e_dto.chromosome import Chromosome
from mv64e_dto.coding import Coding
from pydantic import ValidationError
import pytest

DUMMY_GENE_CODING = Coding(code="GENE_3", display="Partner 3 Gene")


def test_partner3_prime_initialization():
    p3 = DnaFusionFusionPartner3Prime(
        chromosome=Chromosome.CHR15,
        gene=DUMMY_GENE_CODING,
        position=1234567.0
    )
    assert p3.chromosome == Chromosome.CHR15
    assert p3.gene.code == "GENE_3"
    assert p3.position == 1234567.0


def test_partner3_prime_alias_input_and_serialization():
    data = {
        "chromosome": "chr19",
        "position": 98765.12
    }
    p3 = DnaFusionFusionPartner3Prime(**data)

    # Überprüfung der Deserialisierung
    assert p3.chromosome == Chromosome.CHR19
    assert p3.position == 98765.12

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = p3.model_dump(by_alias=True)
    assert dump["chromosome"] == "chr19"
    assert dump["position"] == 98765.12


def test_partner3_prime_missing_required_position():
    data = {"chromosome": "chr1"}
    with pytest.raises(ValidationError):
        DnaFusionFusionPartner3Prime(**data)