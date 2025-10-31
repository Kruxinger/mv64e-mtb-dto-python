from mv64e_dto.dna_fusion import DnaFusion
from mv64e_dto.reference import Reference
from mv64e_dto.variant_external_id import VariantExternalId
from mv64e_dto.external_id_system import ExternalIdSystem
from mv64e_dto.dna_fusion_fusion_partner3_prime import DnaFusionFusionPartner3Prime
from mv64e_dto.dna_fusion_fusion_partner5_prime import DnaFusionFusionPartner5Prime
from mv64e_dto.chromosome import Chromosome
from mv64e_dto.coding import Coding
from pydantic import ValidationError
import pytest


# from mv64e_dto.base_variant_localization_coding import BaseVariantLocalizationCoding # Muss existieren

# Simuliere BaseVariantLocalizationCoding für den Test, falls es nicht verfügbar ist
class BaseVariantLocalizationCoding:
    pass


# Dummy-Daten
DUMMY_REF = Reference(id="pat_d", type="Patient")
DUMMY_EXT_ID = VariantExternalId(system=ExternalIdSystem.ENSEMBL_ORG, value="EID1")
DUMMY_PARTNER_3 = DnaFusionFusionPartner3Prime(chromosome=Chromosome.CHR1, position=100.0)
DUMMY_PARTNER_5 = DnaFusionFusionPartner5Prime(chromosome=Chromosome.CHR2, position=200.0)


def test_dna_fusion_initialization():
    df = DnaFusion(
        id="fusion_test",
        reported_num_reads=500,
        patient=DUMMY_REF,
        fusion_partner3_prime=DUMMY_PARTNER_3,
        fusion_partner5_prime=DUMMY_PARTNER_5,
        external_ids=[DUMMY_EXT_ID]
    )
    assert df.id == "fusion_test"
    assert df.reported_num_reads == 500
    assert df.patient.id == "pat_d"
    assert df.fusion_partner3_prime.chromosome == Chromosome.CHR1
    assert df.external_ids[0].value == "EID1"


def test_dna_fusion_alias_input_and_serialization():
    data = {
        "id": "fusion_b",
        "reportedNumReads": 1000,
        "fusionPartner3prime": {"chromosome": "chr10", "position": 50000.0},
        "fusionPartner5prime": {"chromosome": "chr11", "position": 60000.0}
    }
    df = DnaFusion(**data)

    # Überprüfung der Deserialisierung
    assert df.reported_num_reads == 1000
    assert df.fusion_partner3_prime.chromosome == Chromosome.CHR10

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = df.model_dump(by_alias=True)
    assert dump["reportedNumReads"] == 1000
    assert dump["fusionPartner5prime"]["chromosome"] == "chr11"


def test_dna_fusion_missing_required_reads():
    data = {"id": "fusion_c"}
    with pytest.raises(ValidationError):
        DnaFusion(**data)