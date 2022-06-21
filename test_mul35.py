from .mul35 import find_multiple

def test_success():
    assert find_multiple(0) == 0
    assert find_multiple(10) == 23
    assert find_multiple(20) == 78
    assert find_multiple(1000) == 233168

def test_edge():
    # fail
    try:
        assert find_multiple(10.1) == 0
        assert False
    except Exception:
        assert True
    try:
        assert find_multiple(-1) == 0
        assert False
    except Exception:
        assert True
