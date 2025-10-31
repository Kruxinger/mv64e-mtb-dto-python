from mv64e_dto.rna_fusion import RnaFusion
from mv64e_dto.rna_fusion_fusion_partner_3prime import RnaFusionFusionPartner3Prime
from mv64e_dto.rna_fusion_fusion_partner_5prime import RnaFusionFusionPartner5Prime
from mv64e_dto.rna_fusion_strand import RnaFusionStrand

# Dummy-Partner-Daten
DUMMY_PARTNER_3P = RnaFusionFusionPartner3Prime(
    exon_id="10",
    gene={"code": "ETV6"},
    position=100.5,
    strand=RnaFusionStrand.NEGATIVE
)
DUMMY_PARTNER_5P = RnaFusionFusionPartner5Prime(
    exon_id="12",
    gene={"code": "NTRK1"},
    strand=RnaFusionStrand.POSITIVE
)

def test_rna_fusion_deserialization():
    data = {
        "id": "rna-fus1",
        "effect": "Fusion",
        "reportedNumReads": 1500,
        "fusionPartner3prime": {
            "exonId": "8",
            "strand": "+",
            "position": 55.0
        },
        "fusionPartner5prime": {
            "exonId": "1",
            "strand": "-"
        }
    }
    fusion = RnaFusion(**data)

    assert fusion.id == "rna-fus1"
    assert fusion.reported_num_reads == 1500
    assert fusion.fusion_partner_3prime.exon_id == "8"
    assert fusion.fusion_partner_3prime.strand == RnaFusionStrand.POSITIVE
    assert fusion.fusion_partner_5prime.strand == RnaFusionStrand.NEGATIVE

def test_rna_fusion_serialization():
    fusion = RnaFusion(
        id="rna-fus2",
        fusion_partner_3prime=DUMMY_PARTNER_3P,
        fusion_partner_5prime=DUMMY_PARTNER_5P
    )
    dump = fusion.model_dump(by_alias=True, exclude_none=True)
    assert dump["fusionPartner3prime"]["exonId"] == "10"
    assert dump["fusionPartner5prime"]["strand"] == "+"