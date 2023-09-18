tests = []


def test_all():
    fails = []
    for test in tests:
        if not test():
            fails.append(test)
    return fails
