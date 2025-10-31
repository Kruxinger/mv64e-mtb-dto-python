from datetime import date
from mv64e_dto.somatic_ngs_report import SomaticNgsReport
from mv64e_dto.ngs_report_metadata import NgsReportMetadata
from mv64e_dto.reference import Reference

# Dummy-Daten
DUMMY_METADATA = NgsReportMetadata(
    kit_type="TruSight Oncology 500",
    sequencer="Illumina NovaSeq"
)
DUMMY_PATIENT_REF = Reference(reference="Patient/pat1")
DUMMY_SPECIMEN_REF = Reference(reference="Specimen/s1")

def test_somatic_ngs_report_deserialization():
    data = {
        "id": "ngsr1",
        "issuedOn": "2024-09-01",
        "metadata": [
            {"kitType": "TSO500", "pipeline": "v1.2"}
        ],
        "patient": {"reference": "Patient/p2"},
        "results": {"tumorCellularity": "70%"}, # Dummy NgsReportResults
        "type": {"code": "WES"} # Dummy NgsReportCoding
    }
    report = SomaticNgsReport(**data)

    assert report.id == "ngsr1"
    assert report.issued_on == date(2024, 9, 1)
    assert len(report.metadata) == 1
    assert report.metadata[0].pipeline == "v1.2"
    assert report.patient.reference == "Patient/p2"
    assert report.results["tumorCellularity"] == "70%"

def test_somatic_ngs_report_serialization():
    report = SomaticNgsReport(
        id="ngsr2",
        issued_on=date(2023, 1, 15),
        metadata=[DUMMY_METADATA],
        patient=DUMMY_PATIENT_REF,
        specimen=DUMMY_SPECIMEN_REF
    )
    dump = report.model_dump(by_alias=True, exclude_none=True)
    assert dump["issuedOn"] == "2023-01-15"
    assert dump["metadata"][0]["sequencer"] == "Illumina NovaSeq"
    assert dump["patient"]["reference"] == "Patient/pat1"