from water import water_column_height, \
    pressure_gain_from_water_height, \
    pressure_loss_from_pipe, \
    pressure_loss_from_fittings, \
    reynolds_number, \
    pressure_loss_from_pipe_reduction, \
    kpa_to_psi
import pytest


def test_water_column_height():
    assert water_column_height(10, 4) == 10 + (3 * 4) / 4

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(10) == approx(97861.7, rel=1e-3)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.3, 100, 0.02, 2) == approx(-13.309, rel=1e-2)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(2, 3) == approx(-0.239, rel=1e-2)

def test_reynolds_number():
    assert reynolds_number(0.3, 2) == approx(179, rel=1e-2)

def test_pressure_loss_from_pipe_reduction():
    reynolds = reynolds_number(0.3, 2)
    assert pressure_loss_from_pipe_reduction(0.3, 2, reynolds, 0.1) == approx(-0.222, rel=1e-2)

def test_kpa_to_psi():
    assert kpa_to_psi(100) == approx(14.5038, rel=1e-4)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])    