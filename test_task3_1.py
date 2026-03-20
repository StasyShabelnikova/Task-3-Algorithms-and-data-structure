import pytest
from task_3_1 import sqrt_num

def test_basic():
    n = 8
    result = sqrt_num(n)
    assert result == 2

def test_accurancy():
    n = 9
    result = sqrt_num(n)
    assert result == 3

def test_zero():
    n = 0
    result = sqrt_num (n)
    assert result == 0

def test_fault():
    with pytest.raises(ValueError):
        sqrt_num(-1)