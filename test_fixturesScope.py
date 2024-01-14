import pytest

@pytest.fixture(scope="session", autouse = True)
def setupSession():
    print("\n Setup Session")

@pytest.fixture(scope="module", autouse = True)
def setupModule():
    print("\n Setup Module")

@pytest.fixture(scope="function", autouse = True)
def setupfunction():
    print("\n Setup function")

def test1():
    print("\n Execute Test1!")
    assert True

def test2():
    print("\n Execute Test2!")
    assert True


