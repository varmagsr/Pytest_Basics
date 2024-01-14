from pytest import raises

def rasievalueException():
    raise ValueError

def test_exception():
    with raises(ValueError):
        rasievalueException()
