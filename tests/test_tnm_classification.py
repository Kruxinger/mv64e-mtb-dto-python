from mv64e_dto.tnm_classification import TnmClassification
from mv64e_dto.coding import Coding

# Dummy-Daten
DUMMY_T_CODING = Coding(code="T3", display="Tumorgröße 3")
DUMMY_N_CODING = Coding(code="N1", display="Lymphknotenbefall")
DUMMY_M_CODING = Coding(code="M0", display="Keine Fernmetastasen")


def test_tnm_initialization_and_access():
    tnm = TnmClassification(
        tumor=DUMMY_T_CODING,
        nodes=DUMMY_N_CODING,
        metastasis=DUMMY_M_CODING
    )
    assert tnm.tumor.code == "T3"
    assert tnm.nodes.code == "N1"
    assert tnm.metastasis.code == "M0"


def test_tnm_serialization_and_deserialization():
    data = {
        "tumor": {"code": "T4a", "system": "http://loinc.org"},
        "nodes": {"code": "N2"},
        "metastasis": {"code": "M1b"}
    }
    tnm = TnmClassification(**data)

    # Überprüfung der Deserialisierung
    assert tnm.tumor.code == "T4a"
    assert tnm.tumor.system == "http://loinc.org"
    assert tnm.metastasis.code == "M1b"

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = tnm.model_dump(by_alias=True, exclude_none=True)
    assert dump["tumor"]["code"] == "T4a"
    assert dump["nodes"]["code"] == "N2"