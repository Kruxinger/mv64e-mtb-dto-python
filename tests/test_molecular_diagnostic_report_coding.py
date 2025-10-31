from mv64e_dto.molecular_diagnostic_report_coding import MolecularDiagnosticReportCoding
from mv64e_dto.molecular_diagnostic_report_coding_code import MolecularDiagnosticReportCodingCode

DUMMY_CODE = MolecularDiagnosticReportCodingCode.GENOME_SHORT_READ


def test_mdr_coding_initialization():
    coding = MolecularDiagnosticReportCoding(
        code=DUMMY_CODE,
        display="Whole Genome Sequencing (Short Read)",
        system="http://mtb-standards.de/codesystem/sequencing-method"
    )
    assert coding.code == MolecularDiagnosticReportCodingCode.GENOME_SHORT_READ
    assert coding.display.startswith("Whole Genome")


def test_mdr_coding_serialization_and_deserialization():
    data = {
        "code": "FISH",
        "display": "Fluorescence In Situ Hybridization",
        "version": "v1.0"
    }
    coding = MolecularDiagnosticReportCoding(**data)

    # Überprüfung der Deserialisierung
    assert coding.code == MolecularDiagnosticReportCodingCode.FISH

    # Überprüfung der Serialisierung (Alias-Namen)
    dump = coding.model_dump(by_alias=True)
    assert dump["code"] == "FISH"
    assert dump["version"] == "v1.0"