## This test is show how to auto run the setup fixture insterd of calling it from each test using ""autouse=True"

import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\n setup")


def test1():
    print("\n Executing Test1!")
    assert True

def test2():
    print("\n Executing Test2!")
    assert True

