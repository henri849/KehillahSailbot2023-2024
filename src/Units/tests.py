def test_all():
    tests = [test_my_func]
    fails = []
    for test in tests:
        if not test():
            fails.append(test)
    return fails


def test_my_func():
    return False