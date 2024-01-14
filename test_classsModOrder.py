import pytest

class TestClass:
    @classmethod
    def setup_class(cls):

        print("\n Setup Testclass!")

    @classmethod
    def teardown_class(cls):
        print("\n teardown Testclass")

    def setup_method(self, method):
        if method == self.test1:
            print("\n Setting up test1!")
        elif method == self.test2:
            print("\n Setting up test2!")
        else:
            print("\n Setting up unknow test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\n Tearing down test1!")
        elif method == self.test2:
            print("\n Tearing down test2!")
        else:
            print("\n Tearing down unknow test!")

    def test1(self):
        print("\n Executing Test1")
        assert True

    def test2(self):
        print("\n Executing Test2")
        assert True
