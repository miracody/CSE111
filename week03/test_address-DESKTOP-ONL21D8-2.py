from address import test_extract_city, \
        test_extract_state, test_extract_zipcode
import pytest


def test_extract_city():
    assert test_extract_city("123 Main St, Springfield, IL 62701")=="Springfield"
    assert test_extract_city("456 Oak St, Metropolis, NY 10001")=="Metropolis"


def test_extract_state():
    assert test_extract_state("123 Main St, Springfield, IL 62701")=="IL"
    assert test_extract_state("456 Oak St, Metropolis, NY 10001")=="NY"


def test_extract_zipcode():
    assert test_extract_zipcode("123 Main St, Springfield, IL 62701")=="62701"
    assert test_extract_zipcode("456 Oak St, Metropolis, NY 10001")=="10001"

pytest.main(["-v", "--tb=line", "-rN", __file__])