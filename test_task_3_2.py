import pytest
from task_3_2 import copy_time 

def test_basic():
    assert copy_time(5, 1, 2) == 4

def test_fault():
    with pytest.raises(ValueError):
        copy_time(-1, 8, 7)

def test_one_page():
    assert copy_time(1, 5, 9) == 5

def test_same_time():
    assert copy_time(7, 2, 2) == 8

def test_even_page():
    assert copy_time(6, 2, 2) == 8

def test_zero_page():
    assert copy_time(0, 4, 7) == 0
