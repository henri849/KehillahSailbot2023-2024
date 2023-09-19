def test(f, ins, expected):
    assert type(ins) == list, "test accepts a list of inputs"
    assert type(expected) == list, "test accepts a list of outputs"
    assert len(ins) == len(expected), "each input object must map to exactly one output"
    actual = [f(i) for i in ins]
    for i in range(len(expected)):
        if expected[i] != actual[i]:
            return False, str(i) + " test of " + f.__qualname__ + " failed! " + f.__qualname__ + "(" + str(ins[i]) +\
                   ") should return " + str(expected[i]) + ", returned " + str(actual[i]) + "."
    return True, "Test passed."
