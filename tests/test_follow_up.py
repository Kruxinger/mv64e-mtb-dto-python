from datetime import date, datetime
from mv64e_dto.follow_up import FollowUp
from mv64e_dto.reference import Reference
from mv64e_dto.follow_up_patient_status_coding import FollowUpPatientStatusCoding
from mv64e_dto.follow_up_patient_status_coding_code import FollowUpPatientStatusCodingCode

# Dummy-Daten
DUMMY_REF = Reference(id="pat_f", type="Patient")
DUMMY_STATUS = FollowUpPatientStatusCoding(code=FollowUpPatientStatusCodingCode.LOST_TO_FU)


def test_follow_up_initialization():
    d = date(2023, 11, 25)
    lcd = datetime(2023, 11, 20, 10, 0, 0)

    f = FollowUp(
        date=d,
        last_contact_date=lcd,
        patient=DUMMY_REF,
        patient_status=DUMMY_STATUS
    )
    assert f.date == d
    assert f.last_contact_date == lcd
    assert f.patient.id == "pat_f"
    assert f.patient_status.code == FollowUpPatientStatusCodingCode.LOST_TO_FU


def test_follow_up_date_serialization_and_deserialization():
    # Deserialisierung von JSON (String-Input)
    data = {
        "date": "2024-06-15",
        "lastContactDate": "2024-06-10T12:00:00Z"
    }
    f = FollowUp(**data)

    # Überprüfung der Deserialisierungstypen und -werte
    assert f.date == date(2024, 6, 15)
    assert f.last_contact_date == datetime(2024, 6, 10, 12, 0, 0)

    # Überprüfung der Serialisierung (Alias-Namen und korrekte Formate)
    dump = f.model_dump(by_alias=True, mode='json')
    assert dump["date"] == "2024-06-15"  # Datum-Format
    assert dump["lastContactDate"] == "2024-06-10T12:00:00Z"  # ISO-Datetime-Format