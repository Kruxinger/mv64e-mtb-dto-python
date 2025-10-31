from mv64e_dto.tumor_specimen import TumorSpecimen
from mv64e_dto.tumor_specimen_coding_code import TumorSpecimenCodingCode
from mv64e_dto.tumor_specimen_coding import TumorSpecimenCoding
from mv64e_dto.reference import Reference

# Dummy-Daten
DUMMY_TYPE = TumorSpecimenCoding(code=TumorSpecimenCodingCode.FFPE, display="FFPE-Gewebe")

def test_tumor_specimen_deserialization():
    data = {
        "id": "ts1",
        "type": {"code": "liquid-biopsy", "system": "http://mtb-codesystem.de/specimen-type"},
        "patient": {"reference": "Patient/p3"},
        "collection": {"method": "BIOP", "date": "2024-01-01"}, # Dummy Collection
    }
    specimen = TumorSpecimen(**data)

    assert specimen.id == "ts1"
    assert specimen.type.code == TumorSpecimenCodingCode.LIQUID_BIOPSY
    assert specimen.patient.reference == "Patient/p3"
    assert specimen.collection["method"] == "BIOP"

def test_tumor_specimen_serialization():
    specimen = TumorSpecimen(
        id="ts2",
        type=DUMMY_TYPE,
        diagnosis=Reference(reference="Diagnosis/d4")
    )
    dump = specimen.model_dump(by_alias=True, exclude_none=True)
    assert dump["id"] == "ts2"
    assert dump["type"]["code"] == "FFPE"
    assert dump["diagnosis"]["reference"] == "Diagnosis/d4"