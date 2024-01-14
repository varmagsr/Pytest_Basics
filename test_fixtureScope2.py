import pytest

@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\n Setup Module2")

@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\n Setup Class2")

@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\n Setup function2")

class TestClass:
    def test_it(self):
        print("\n test it")
        assert True

    def test_it2(self):
        print("\n test it2")
        assert True
