"""Explicit paper parameters for the Monks et al. base scenario."""

from __future__ import annotations

from .config import ArrivalParameter, Destination, LognormalSummary, Ward
from .patients import PatientGroup


ACUTE_ARRIVAL_MEAN_DAYS: dict[PatientGroup, ArrivalParameter] = {
    PatientGroup.STROKE: ArrivalParameter(
        mean_interarrival_days=1.2,
        source_note="Figure 2 acute admission stream, 2013/14",
    ),
    PatientGroup.TIA: ArrivalParameter(
        mean_interarrival_days=9.3,
        source_note="Figure 2 acute admission stream, 2013/14",
    ),
    PatientGroup.COMPLEX_NEURO: ArrivalParameter(
        mean_interarrival_days=3.6,
        source_note="Figure 2 acute admission stream, 2013/14",
    ),
    PatientGroup.OTHER: ArrivalParameter(
        mean_interarrival_days=3.2,
        source_note="Figure 2 acute admission stream, 2013/14",
    ),
}


REHAB_EXTERNAL_ARRIVAL_MEAN_DAYS: dict[PatientGroup, ArrivalParameter] = {
    PatientGroup.STROKE: ArrivalParameter(
        mean_interarrival_days=21.8,
        source_note="Figure 2 transfer from elsewhere to rehab, 2013/14",
    ),
    PatientGroup.COMPLEX_NEURO: ArrivalParameter(
        mean_interarrival_days=31.7,
        source_note="Figure 2 transfer from elsewhere to rehab, 2013/14",
    ),
    PatientGroup.OTHER: ArrivalParameter(
        mean_interarrival_days=28.6,
        source_note="Figure 2 transfer from elsewhere to rehab, 2013/14",
    ),
}


LENGTH_OF_STAY: dict[Ward, dict[str, LognormalSummary]] = {
    Ward.ACUTE: {
        "stroke_no_esd": LognormalSummary(7.4, 8.6, 4.0, 1.0, 23.0, 2.0, 9.0, "Appendix Table S2 acute LOS"),
        "stroke_esd": LognormalSummary(4.6, 4.8, 3.0, 1.0, 11.0, 2.0, 6.0, "Appendix Table S2 acute LOS"),
        "stroke_mortality": LognormalSummary(7.0, 8.7, 4.0, 0.5, 22.0, 2.0, 8.0, "Appendix Table S2 acute LOS"),
        "tia": LognormalSummary(1.8, 2.3, 1.0, 0.5, 4.0, 1.0, 2.0, "Appendix Table S2 acute LOS"),
        "complex_neurological": LognormalSummary(4.0, 5.0, 2.0, 0.5, 13.6, 1.0, 5.0, "Appendix Table S2 acute LOS"),
        "other": LognormalSummary(3.8, 5.2, 2.0, 0.5, 12.1, 1.0, 5.0, "Appendix Table S2 acute LOS"),
    },
    Ward.REHAB: {
        "stroke_no_esd": LognormalSummary(28.4, 27.2, 20.0, 3.0, 86.9, 9.0, 38.0, "Appendix Table S2 rehab LOS"),
        "stroke_esd": LognormalSummary(30.3, 23.1, 22.0, 6.0, 78.0, 13.8, 44.0, "Appendix Table S2 rehab LOS"),
        "complex_neurological": LognormalSummary(27.6, 28.4, 18.0, 2.5, 88.5, 8.0, 36.0, "Appendix Table S2 rehab LOS"),
        "other": LognormalSummary(16.1, 14.1, 11.5, 1.0, 43.0, 5.8, 24.3, "Appendix Table S2 rehab LOS"),
        "tia": LognormalSummary(18.7, 23.5, 11.0, 1.1, 41.6, 5.5, 28.0, "Appendix Table S2 rehab LOS"),
    },
}


ROUTING_FROM_ACUTE: dict[PatientGroup, dict[Destination, float]] = {
    PatientGroup.STROKE: {Destination.REHAB: 0.24, Destination.ESD: 0.13, Destination.OTHER: 0.63},
    PatientGroup.TIA: {Destination.REHAB: 0.01, Destination.ESD: 0.01, Destination.OTHER: 0.98},
    PatientGroup.COMPLEX_NEURO: {Destination.REHAB: 0.11, Destination.ESD: 0.05, Destination.OTHER: 0.84},
    PatientGroup.OTHER: {Destination.REHAB: 0.05, Destination.ESD: 0.10, Destination.OTHER: 0.85},
}


ROUTING_FROM_REHAB: dict[PatientGroup, dict[Destination, float]] = {
    PatientGroup.STROKE: {Destination.ESD: 0.40, Destination.OTHER: 0.60},
    PatientGroup.TIA: {Destination.ESD: 0.00, Destination.OTHER: 1.00},
    PatientGroup.COMPLEX_NEURO: {Destination.ESD: 0.09, Destination.OTHER: 0.91},
    PatientGroup.OTHER: {Destination.ESD: 0.13, Destination.OTHER: 0.88},
}


BASE_CAPACITY_BEDS: dict[Ward, int] = {
    Ward.ACUTE: 10,
    Ward.REHAB: 12,
}
