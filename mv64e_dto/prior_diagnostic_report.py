from typing import Optional, List, Dict, Any
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.molecular_diagnostic_report_coding import MolecularDiagnosticReportCoding
from mv64e_dto.reference import Reference

class PriorDiagnosticReport(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    issued_on: Optional[date] = Field(default=None, alias="issuedOn")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    performer: Optional[Reference] = Field(default=None, alias="performer")
    results: Optional[List[str]] = Field(default=None, alias="results") # List<String> in Java
    specimen: Optional[Reference] = Field(default=None, alias="specimen")
    type: Optional[MolecularDiagnosticReportCoding] = Field(default=None, alias="type") # PLACEHOLDER: MolecularDiagnosticReportCoding

    model_config = {"populate_by_name": True, "from_attributes": True}