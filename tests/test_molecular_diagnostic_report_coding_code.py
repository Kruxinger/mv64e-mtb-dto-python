from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.molecular_diagnostic_report_coding_code import MolecularDiagnosticReportCodingCode

class CodeTestModel(BaseModel):
    code: MolecularDiagnosticReportCodingCode

def test_code_values():
    """Prüft die Werte, die Klein- und Großbuchstaben sowie Bindestriche enthalten."""
    assert MolecularDiagnosticReportCodingCode.GENOME_LONG_READ.value == "genome-long-read"
    assert MolecularDiagnosticReportCodingCode.PCR.value == "PCR"

def test_code_serialization():
    model = CodeTestModel(code=MolecularDiagnosticReportCodingCode.EXOME)
    dumped_data = model.model_dump()
    assert dumped_data["code"] == "exome"

def test_code_deserialization_success():
    data = {"code": "fusion-panel"}
    model = CodeTestModel(**data)
    assert model.code == MolecularDiagnosticReportCodingCode.FUSION_PANEL