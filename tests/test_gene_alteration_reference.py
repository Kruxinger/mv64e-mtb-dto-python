from mv64e_dto.gene_alteration_reference import GeneAlterationReference
from mv64e_dto.coding import Coding
from mv64e_dto.reference import Reference

DUMMY_CODING = Coding(code="GENE_A")
DUMMY_REF = Reference(id="var_1", type="Variant")

def test_gene_alteration_reference_initialization():
    g = GeneAlterationReference(
        display="BRAF V600E Reference",
        gene=DUMMY_CODING,
        variant=DUMMY_REF
    )
    assert g.display == "BRAF V600E Reference"
    assert g.gene.code == "GENE_A"
    assert g.variant.id == "var_1"

def test_gene_alteration_reference_alias_input():
    data = {
        "display": "Ref 2",
        "gene": {"code": "GENE_B", "system": "S2"},
        "variant": {"id": "var_2", "type": "Variant"}
    }
    g = GeneAlterationReference(**data)
    assert g.display == "Ref 2"
    assert g.gene.system == "S2"
    assert g.variant.type == "Variant"