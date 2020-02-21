from task1 import json_eq
import json
import pytest
import math

test_parameters = (
    ('a', 'a', True),
    ('A', 'a', False),
    ('a', 'b', False),
    (1, 1, True),
    (1, -1, False),
    (1, 2, False),
    (1, None, False),
    (None, None, True),
    (math.nan, math.nan, False),
    (math.nan, 0.1, False),
    (math.inf, math.inf, True),
    (math.inf, 0.1, False),
    (1.0, 1.0, True),
    (0.0, 0.0, True),
    (1.22222, 1.22222, True),
    (1.222223, 1.222222, True),
    (1.222232, 1.222222, False),
    ([], [], True),
    (['a'], ['a'], True),
    ([1], [], False),
    ({1:2}, {1:2}, True),
    ({1:2}, {1:3}, False),
    ([{1:2}, 's', {1: ['1', 2]}], [{1:2}, 's', {1: ['1', 2]}], True),
    ([{1:2}, 's', {1: ['1', 2]}], [{1:2}, 's', {1: ['1', 2.]}], False)
)


@pytest.mark.parametrize("one,two,result", test_parameters)
def test_json_equality(one, two, result):
    one = json.dumps(one)
    two = json.dumps(two)
    assert json_eq.json_equals(one, two) == result
    assert json_eq.json_equals(two, one) == result
