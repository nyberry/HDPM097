from stroke_sim.config import Destination, Ward
from stroke_sim.parameters import (
    ACUTE_ARRIVAL_MEAN_DAYS,
    BASE_CAPACITY_BEDS,
    LENGTH_OF_STAY,
    REHAB_EXTERNAL_ARRIVAL_MEAN_DAYS,
    ROUTING_FROM_ACUTE,
    ROUTING_FROM_REHAB,
)
from stroke_sim.patients import PatientGroup


def test_acute_arrival_means_match_figure_2() -> None:
    assert ACUTE_ARRIVAL_MEAN_DAYS[PatientGroup.STROKE].mean_interarrival_days == 1.2
    assert ACUTE_ARRIVAL_MEAN_DAYS[PatientGroup.TIA].mean_interarrival_days == 9.3
    assert ACUTE_ARRIVAL_MEAN_DAYS[PatientGroup.COMPLEX_NEURO].mean_interarrival_days == 3.6
    assert ACUTE_ARRIVAL_MEAN_DAYS[PatientGroup.OTHER].mean_interarrival_days == 3.2


def test_rehab_external_arrivals_exclude_tia() -> None:
    assert PatientGroup.TIA not in REHAB_EXTERNAL_ARRIVAL_MEAN_DAYS
    assert REHAB_EXTERNAL_ARRIVAL_MEAN_DAYS[PatientGroup.STROKE].mean_interarrival_days == 21.8


def test_length_of_stay_contains_expected_groups() -> None:
    assert LENGTH_OF_STAY[Ward.ACUTE]["stroke_esd"].mean == 4.6
    assert LENGTH_OF_STAY[Ward.REHAB]["complex_neurological"].p95 == 88.5


def test_acute_routing_rows_sum_to_one() -> None:
    for row in ROUTING_FROM_ACUTE.values():
        assert sum(row.values()) == 1.0


def test_rehab_routing_rows_are_near_one_despite_published_rounding() -> None:
    for patient_group, row in ROUTING_FROM_REHAB.items():
        total = sum(row.values())
        if patient_group is PatientGroup.OTHER:
            assert abs(total - 1.01) < 1e-9
        else:
            assert total == 1.0


def test_base_capacity_matches_paper() -> None:
    assert BASE_CAPACITY_BEDS[Ward.ACUTE] == 10
    assert BASE_CAPACITY_BEDS[Ward.REHAB] == 12
    assert ROUTING_FROM_REHAB[PatientGroup.STROKE][Destination.ESD] == 0.40
