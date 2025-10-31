from enum import Enum
from pydantic import BaseModel, ValidationError
import pytest
from mv64e_dto.chromosome import Chromosome


class EnumTestModel(BaseModel):
    # Wir nutzen ein Test-Modell, um zu prüfen, wie Pydantic die Enum behandelt.
    chrom: Chromosome


def test_chromosome_values():
    """Überprüft, ob die Enum-Werte korrekt auf die JSON-Strings abgebildet werden."""
    assert Chromosome.CHR1.value == "chr1"
    assert Chromosome.CHR_X.value == "chrX"
    assert Chromosome.CHR_MT.value == "chrMT"
    assert isinstance(Chromosome.CHR1, str)


def test_chromosome_serialization():
    """Überprüft die Serialisierung (Python-Objekt -> JSON)."""
    model = EnumTestModel(chrom=Chromosome.CHR10)
    # Pydantic serialisiert den Wert (value) der Enum
    dumped_data = model.model_dump()
    assert dumped_data["chrom"] == "chr10"


def test_chromosome_deserialization_success():
    """Überprüft die Deserialisierung (JSON-String -> Python-Enum)."""
    data = {"chrom": "chr22"}
    model = EnumTestModel(**data)
    # Pydantic kann den String automatisch dem korrekten Enum-Wert zuordnen
    assert model.chrom == Chromosome.CHR22
    assert model.chrom.name == "CHR22" # Überprüfung des Enum-Namens


def test_chromosome_deserialization_failure():
    """Überprüft die Fehlerbehandlung bei ungültigem Wert."""
    data = {"chrom": "invalid_chromosome"}
    with pytest.raises(ValidationError):
        # Pydantic löst einen ValidationError aus, wenn der String kein gültiger Enum-Wert ist
        EnumTestModel(**data)