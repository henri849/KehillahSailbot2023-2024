from main import *


def test_all():
    tests = [test_my_func]
    fails = []
    for test in tests:
        result, message = test()
        if not result:
            fails.append(message)
    return fails


def test_my_func():
    try:
        assert my_func() == 14, "failed"

        return True, ""
    except Exception as e:
        return False, e
