from task_3_3 import feed_animals

def test_basic():
    food = [1, 4, 3, 8]
    animals = [8, 2, 3, 2]
    assert feed_animals(animals, food) == 3

def test_zeroAni():
    food = [2, 4, 3, 1, 5]
    animals = []
    assert feed_animals(animals, food) == 0

def test_zeroFood():
    food = []
    animals = [1, 4, 2, 8]
    assert feed_animals(animals, food) == 0

def test_zero():
    food = []
    animals = []
    assert feed_animals(animals, food) == 0

def test_more_food():
    assert feed_animals([1, 2], [1, 3, 1, 4, 5]) == 2

def test_no_match():
    assert feed_animals([6, 7, 8], [1, 3, 1, 5]) == 0
    