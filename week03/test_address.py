from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("123 Main St, Springfield, IL 62701") == "Springfield"
    assert extract_city("456 Oak St, Metropolis, NY 10001") == "Metropolis"

def test_extract_state():
    assert extract_state("123 Main St, Springfield, IL 62701") == "IL"
    assert extract_state("456 Oak St, Metropolis, NY 10001") == "NY"

def test_extract_zipcode():
    assert extract_zipcode("123 Main St, Springfield, IL 62701") == "62701"
    assert extract_zipcode("456 Oak St, Metropolis, NY 10001") == "10001"

pytest.main(["-v", "--tb=line", "-rN", __file__])