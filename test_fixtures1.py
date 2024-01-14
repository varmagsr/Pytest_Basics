import pytest

@pytest.fixture()
def setup():
    print("\n setup")

##1st way to get setup fixtue to execute before test case, to call setup in "test1(setup)"
def test1(setup):
    print("\n Executing Test1!")
    assert True
## @nd way to call is use "@pytest.mark.usefixtures("setup")" get setup funcation executed before test case2
@pytest.mark.usefixtures("setup")
def test2():
    print("\n Executing Test2!")
    assert True

