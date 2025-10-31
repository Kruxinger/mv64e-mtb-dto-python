from datetime import date
import pytest
from mv64e_dto.claim import Claim
from mv64e_dto.reference import Reference
from mv64e_dto.claim_stage_coding import ClaimStageCoding
from mv64e_dto.claim_stage_coding_code import ClaimStageCodingCode
from mv64e_dto.atc_unregistered_medication_coding import AtcUnregisteredMedicationCoding  # Achtung: Platzhalter

# Erstellen von Dummy-Daten für die abhängigen DTOs
DUMMY_PATIENT_REF = Reference(id="pat1", type="Patient")
DUMMY_STAGE_CODING = ClaimStageCoding(code=ClaimStageCodingCode.INITIAL_CLAIM, display="Init")


def test_claim_initialization():
    c = Claim(
        id="c123",
        issued_on=date(2025, 10, 24),
        patient=DUMMY_PATIENT_REF,
        stage=DUMMY_STAGE_CODING
    )
    assert c.id == "c123"
    assert c.issued_on == date(2025, 10, 24)
    assert c.patient.id == "pat1"
    assert c.stage.code == ClaimStageCodingCode.INITIAL_CLAIM


def test_claim_alias_input_and_serialization():
    data = {
        "id": "c456",
        "issuedOn": "2024-01-15",  # JSON-String-Eingabe für Datum
        "patient": {"id": "p2", "type": "Patient"},
        "stage": {"code": "revocation", "system": "sys"}
    }
    c = Claim(**data)

    # Überprüfung der Deserialisierung
    assert c.issued_on == date(2024, 1, 15)
    assert c.patient.id == "p2"
    assert c.stage.code == ClaimStageCodingCode.REVOCATION

    # Überprüfung der Serialisierung (Datum und Alias-Namen)
    dump = c.model_dump(by_alias=True)
    assert dump["id"] == "c456"
    assert dump["issuedOn"] == "2024-01-15"  # Pydantic serialisiert date-Objekte standardmäßig im ISO-Format
    assert dump["stage"]["code"] == "revocation"


# Ein Test, um die Liste der Platzhalter-Medikamente zu überprüfen
def test_claim_requested_medication_list():
    # Da AtcUnregisteredMedicationCoding leer ist, nutzen wir eine leere Instanz
    med_data = [
        {},
        {}
    ]
    data = {
        "id": "c789",
        "requestedMedication": med_data
    }
    c = Claim(**data)

    assert isinstance(c.requested_medication, list)
    assert len(c.requested_medication) == 2
    # Der Typ-Check sollte erfolgreich sein, auch wenn das DTO leer ist
    assert isinstance(c.requested_medication[0], AtcUnregisteredMedicationCoding)