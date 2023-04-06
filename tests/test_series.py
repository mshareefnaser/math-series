import pytest
from series.series import fibonacci, lucas, sum_series
# # 0, 1, 1, 2, 3, 5, 8, 13, ... fibonacci
# # 2, 1, 3, 4, 7, 11, 18, 29, ...lucas


# def test_fibonacci_zero():
#     actual = fibonacci(0)
#     expected = 0
#     assert actual == expected


# def test_fibonacci_3():
#     actual = fibonacci(3)
#     expected = 2
#     assert actual == expected


# def test_fibonacci_4():
#     actual = fibonacci(0)
#     expected = 0
#     assert actual == expected


# def test_lucas_3():
#     actual = lucas(3)
#     expected = 4
#     assert actual == expected

# def test_lucas_6():
#     actual = lucas(6)
#     expected = 18
#     assert actual == expected

def test_fibonacci():
    expected = 3
    actual = fibonacci(4)
    assert actual == expected

def test_fibonacci2():
    expected = 8
    actual = fibonacci(6)
    assert actual == expected

def test_fibonacci3():
    assert fibonacci(7) == 13



def test_lucas():
    expected = 4
    actual = lucas(3)
    assert actual == expected

def test_lucas2():
    expected = 11
    actual = lucas(5)
    assert actual == expected

def test_lucas3():
    expected = 29
    actual = lucas(7)
    assert actual == expected


def test_sum_series():
    assert sum_series(2) == 1

def test_sum_series2():
    expected = 17
    actual = sum_series(7,3,7)
    assert actual == expected
