from task_3_4 import extra_letter

def test_basic():
    assert extra_letter("ab", "cab") == "c"

def test_zero():
    assert extra_letter("dabam", "badam") == None

def test_repeated():
    assert extra_letter("aab", "aaab") == "a"