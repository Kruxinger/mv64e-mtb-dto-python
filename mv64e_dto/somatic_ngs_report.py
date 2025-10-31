from typing import Optional, List, Dict, Any
from datetime import date
from pydantic import BaseModel, Field

from mv64e_dto.ngs_report_coding import NgsReportCoding
from mv64e_dto.ngs_report_results import NgsReportResults
from mv64e_dto.reference import Reference
from mv64e_dto.ngs_report_metadata import NgsReportMetadata

class SomaticNgsReport(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    # @JsonFormat(pattern = "yyyy-MM-dd") -> datetime.date
    issued_on: Optional[date] = Field(default=None, alias="issuedOn")
    metadata: Optional[List[NgsReportMetadata]] = Field(default=None, alias="metadata")
    patient: Optional[Reference] = Field(default=None, alias="patient")
    results: Optional[NgsReportResults] = Field(default=None, alias="results") # PLACEHOLDER: NgsReportResults
    specimen: Optional[Reference] = Field(default=None, alias="specimen")
    type: Optional[Dict[NgsReportCoding]] = Field(default=None, alias="type") # PLACEHOLDER: NgsReportCoding

    model_config = {"populate_by_name": True, "from_attributes": True}