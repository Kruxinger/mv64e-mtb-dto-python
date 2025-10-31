from datetime import date
from mv64e_dto.ihc_report import IhcReport
from mv64e_dto.reference import Reference
from mv64e_dto.ihc_report_results import IhcReportResults
from mv64e_dto.protein_expression import ProteinExpression
from mv64e_dto.coding import Coding
from mv64e_dto.protein_expression_result_coding import ProteinExpressionResultCoding
from mv64e_dto.protein_expression_result_coding_code import ProteinExpressionResultCodingCode
from mv64e_dto.protein_expression_tc_score_coding import ProteinExpressionTcScoreCoding
from mv64e_dto.protein_expression_tc_score_coding_code import ProteinExpressionTcScoreCodingCode

# Dummy-Daten
DUMMY_REF_P = Reference(id="pat_ihc", type="Patient")
DUMMY_REF_S = Reference(id="spec_ihc", type="Specimen")
DUMMY_CODING = Coding(code="PDL1", display="PD-L1")

# Protein Expression Beispiele
PE_PDL1 = ProteinExpression(
    id="pe_1",
    protein=DUMMY_CODING,
    tps_score=50,
    cps_score=75,
    tc_score=ProteinExpressionTcScoreCoding(code=ProteinExpressionTcScoreCodingCode.CODE_3),
    value=ProteinExpressionResultCoding(code=ProteinExpressionResultCodingCode.EXP)
)

PE_MMR = ProteinExpression(
    id="pe_2",
    protein=Coding(code="MLH1"),
    value=ProteinExpressionResultCoding(code=ProteinExpressionResultCodingCode.NOT_EXP)
)

DUMMY_RESULTS = IhcReportResults(
    msi_mmr=[PE_MMR],
    protein_expression=[PE_PDL1]
)


def test_ihc_report_initialization_and_access():
    issue_date = date(2024, 8, 1)
    report = IhcReport(
        id="ihc_rep_1",
        issued_on=issue_date,
        patient=DUMMY_REF_P,
        specimen=DUMMY_REF_S,
        results=DUMMY_RESULTS
    )
    assert report.id == "ihc_rep_1"
    assert report.issued_on == issue_date
    assert len(report.results.protein_expression) == 1
    assert report.results.protein_expression[0].tps_score == 50
    assert report.results.msi_mmr[0].value.code == ProteinExpressionResultCodingCode.NOT_EXP


def test_ihc_report_serialization_and_deserialization():
    data = {
        "id": "ihc_rep_2",
        "issuedOn": "2024-10-31",
        "results": {
            "proteinExpression": [
                {
                    "protein": {"code": "ER"},
                    "tpsScore": 90,
                    "value": {"code": "3+"}
                }
            ]
        }
    }
    report = IhcReport(**data)

    # Überprüfung der Deserialisierung
    assert report.issued_on == date(2024, 10, 31)
    assert report.results.protein_expression[0].tps_score == 90
    assert report.results.protein_expression[0].value.code == ProteinExpressionResultCodingCode.CODE_3PLUS

    # Überprüfung der Serialisierung (Alias-Namen und Datumsformat)
    dump = report.model_dump(by_alias=True, mode='json')
    assert dump["issuedOn"] == "2024-10-31"
    assert dump["results"]["proteinExpression"][0]["tpsScore"] == 90
    assert dump["results"]["proteinExpression"][0]["value"]["code"] == "3+"