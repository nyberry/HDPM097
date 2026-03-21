"""Patient group definitions used by the model."""

from enum import StrEnum


class PatientGroup(StrEnum):
    STROKE = "stroke"
    TIA = "tia"
    COMPLEX_NEURO = "complex_neurological"
    OTHER = "other"
