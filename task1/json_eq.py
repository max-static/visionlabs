import json


def compare(left, right):
    if type(left) != type(right):
        return False
    elif isinstance(left, (int, str, bool)):
        return left == right
    elif isinstance(left, float):
        print(left, right)
        return left == right or abs(left - right) <= 0.00001
    elif isinstance(left, list):
        if len(left) != len(right):
            return False
        return all(compare(i, j) for i, j in zip(left, right))
    elif isinstance(left, dict):
        if left.keys() != right.keys():
            return False
        return all(compare(value, right[key]) for key, value in left.items())
    elif left is None and right is None:
        return True
    else:
        return False


def json_equals(left: str, right: str):
    left = json.loads(left)
    right = json.loads(right)
    return compare(left, right)
