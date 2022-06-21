from .fib import fibonacci

def test_success():
    assert fibonacci(2) == 2
    assert fibonacci(4) == 2
    assert fibonacci(8) == 10
    assert fibonacci(33) == 10
    assert fibonacci(34) == 44
    assert fibonacci(35) == 44
    assert fibonacci(143) == 44
    assert fibonacci(144) == 188
    assert fibonacci(4_000_000) == 4613732

def test_edge():
    assert fibonacci(1) == 0
    try:
        assert fibonacci(0) == 2
        assert False
    except Exception:
        assert True
