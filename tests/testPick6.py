import pytest
from src.pick6 import *


# Test implementation of random number generation in create_random_number
def test_create_random_number():
    ran_num1 = create_random_number()
    assert 1 < ran_num1 < 100


# Test pick6 function
def test_pick6():
    list_of_6 = pick6()
    assert len(list_of_6) == 6
    for i in list_of_6:
        assert type(i) == int


# Test several use cases against expected number of matches
def test_num_matches():
    test_cases = [([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),  # Should return 6 matches
                  ([1, 2, 3, 4, 5, 6], [1, 1, 3, 3, 6, 2]),  # Should return 2 matches
                  ([0, 2, 1, 2, 5, 6], [1, 1, 3, 3, 6, 2]),  # Should return 0 matches
                  ([0, 2, 1, 2, 5, 6], [1, 1, 3, 3, 5, 6])]  # Should return 0 matches

    for idx, case in enumerate(test_cases):
        # idx 0 result: 6 matches
        # idx 1 result: 2 matches
        # idx 2 result: 2 matches

        winning = case[0]
        ticket = case[1]

        matches = num_matches(winning, ticket)
        assert type(winning) == list
        assert type(ticket) == list

        if idx == 0:
            assert matches == 6
        if idx == 1:
            assert matches == 2
        if idx == 2:
            assert matches == 0
        if idx == 3:
            assert matches == 2
        assert type(matches) == int
