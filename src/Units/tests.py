from main import *


def test_all():
    tests = [test_my_func]
    fails = []
    for test in tests:
        result, message = test()
        if not result:
            fails.append(message)
            print(message)
    return fails


def test_my_func():
    try:
        assert my_func() == 14, "failed"

        print("passed")
        return True, ""
    except Exception as e:
        print(e)
        return False, e
