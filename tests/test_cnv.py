from mv64e_dto.cnv import Cnv
from mv64e_dto.chromosome import Chromosome
from mv64e_dto.reference import Reference
from mv64e_dto.cnv_coding import CnvCoding
from mv64e_dto.cnv_coding_code import CnvCodingCode
from mv64e_dto.coding import Coding
from mv64e_dto.end_range import EndRange
from mv64e_dto.start_range import StartRange
from mv64e_dto.variant_external_id import VariantExternalId
from mv64e_dto.external_id_system import ExternalIdSystem

# from mv64e_dto.base_variant_localization_coding import BaseVariantLocalizationCoding # Muss existieren

# Dummy-Daten
DUMMY_REF = Reference(id="pat1", type="Patient")
DUMMY_CNV_TYPE = CnvCoding(code=CnvCodingCode.LOSS)
DUMMY_EXTERNAL_ID = VariantExternalId(system=ExternalIdSystem.ENSEMBL_ORG, value="ENSG123")
DUMMY_CODING = Coding(code="H", system="G")


# Simuliere BaseVariantLocalizationCoding für den Test, falls es nicht verfügbar ist
class BaseVariantLocalizationCoding:
    pass


def test_cnv_initialization():
    c = Cnv(
        id="cnv_a",
        chromosome=Chromosome.CHR1,
        cn_a=1.5,
        total_copy_number=3,
        type=DUMMY_CNV_TYPE,
        patient=DUMMY_REF
    )
    assert c.id == "cnv_a"
    assert c.chromosome == Chromosome.CHR1
    assert c.cn_a == 1.5
    assert c.total_copy_number == 3
    assert c.type.code == CnvCodingCode.LOSS
    assert c.patient.id == "pat1"


def test_cnv_alias_input_and_complex_fields():
    data = {
        "id": "cnv_b",
        "chromosome": "chr12",
        "cnB": 0.5,
        "startRange": {"start": 100.0, "end": 200.0},
        "externalIds": [{"system": "https://cancer.sanger.ac.uk/cosmic", "value": "ID1"}]
    }
    c = Cnv(**data)

    # Überprüfung der Deserialisierung
    assert c.chromosome == Chromosome.CHR12
    assert c.cn_b == 0.5
    assert c.start_range.start == 100.0
    assert c.external_ids[0].value == "ID1"

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = c.model_dump(by_alias=True)
    assert dump["cnB"] == 0.5
    assert dump["startRange"]["end"] == 200.0
    assert dump["externalIds"][0]["system"] == "https://cancer.sanger.ac.uk/cosmic"


def test_cnv_list_fields():
    c = Cnv(
        copy_number_neutral_lo_h=[DUMMY_CODING],
        reported_affected_genes=[DUMMY_CODING, DUMMY_CODING]
    )
    assert len(c.copy_number_neutral_lo_h) == 1
    assert len(c.reported_affected_genes) == 2