# test_my_module.py
from sri_dev_module import   add, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print(f'All assertions passed in test_add')


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5
    print(f'All assertions passed in test_subtract')