from stroke_sim.patients import PatientGroup


def test_patient_groups_include_stroke() -> None:
    assert PatientGroup.STROKE == "stroke"
