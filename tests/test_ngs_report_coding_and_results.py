from mv64e_dto.ngs_report_coding import NgsReportCoding
from mv64e_dto.ngs_report_coding_code import NgsReportCodingCode
from mv64e_dto.ngs_report_results import NgsReportResults


def test_ngs_report_coding_deserialization():
    data = {"code": "panel", "display": "Onkologie-Panel"}
    coding = NgsReportCoding(**data)
    assert coding.code == NgsReportCodingCode.PANEL


def test_ngs_report_results_deserialization_with_dummies():
    data = {
        "tmb": {"value": 15.2},  # Dummy Tmb
        "simpleVariants": [{"gene": "KRAS", "mutation": "G12C"}],  # Dummy Snv
        "tumorCellContent": {"value": 0.6}  # Dummy TumorCellContent
    }
    results = NgsReportResults(**data)

    # Prüfen, ob die Platzhalter korrekt deserialisiert wurden (als Dicts)
    assert results.tmb["value"] == 15.2
    assert results.simple_variants[0]["gene"] == "KRAS"
    assert results.tumor_cell_content["value"] == 0.6

    # Prüfen, ob leere Listen und None-Felder korrekt sind
    assert results.dna_fusions is None
    assert results.brcaness is None


def test_ngs_report_results_serialization():
    results = NgsReportResults(
        dna_fusions=[{"gene1": "NTRK", "gene2": "ETV6"}]
    )
    dump = results.model_dump(by_alias=True, exclude_none=True)
    assert dump["dnaFusions"][0]["gene1"] == "NTRK"