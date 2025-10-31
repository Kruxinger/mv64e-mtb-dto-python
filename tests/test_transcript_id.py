from pydantic import BaseModel
from mv64e_dto.transcript_id import TranscriptId
from mv64e_dto.transcript_id_system import TranscriptIdSystem


class SystemTestModel(BaseModel):
    system: TranscriptIdSystem


def test_system_enum_values():
    assert TranscriptIdSystem.ENSEMBL_ORG.value == "https://www.ensembl.org"


def test_system_deserialization():
    model = SystemTestModel(system="https://www.ncbi.nlm.nih.gov/refseq")
    assert model.system == TranscriptIdSystem.NCBI_NLM_NIH_GOV_REFSEQ


def test_transcript_id_serialization_and_deserialization():
    data = {
        "system": "https://www.ensembl.org",
        "value": "ENST00000371953"
    }
    tid = TranscriptId(**data)

    # Überprüfung der Deserialisierung
    assert tid.system == TranscriptIdSystem.ENSEMBL_ORG
    assert tid.value == "ENST00000371953"

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = tid.model_dump(by_alias=True, exclude_none=True)
    assert dump["system"] == "https://www.ensembl.org"
    assert dump["value"] == "ENST00000371953"