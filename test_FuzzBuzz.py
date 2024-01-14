import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "fizzbuzz"
        return "fizz"
    if isMultiple(value, 5):
        return "buzz"
    return str(value)
def isMultiple(value, mod):
    return (value % mod) == 0

def checkFuzzBuzz( value, expected ):
    retval = fizzBuzz(value)
    assert retval == expected

def test_return1with1PassedIn():
    checkFuzzBuzz(1, "1")

def test_return2with2PassedIn():
    checkFuzzBuzz(2, "2")

def test_returnfizzwith3PassedIn():
    checkFuzzBuzz(3, "fizz")

def test_returnbuzzwith5PassedIn():
    checkFuzzBuzz(5, "buzz")

def test_returnfizzwith6Passedin():
    checkFuzzBuzz(6, "fizz")

def test_returnbuzzwith10Passedin():
    checkFuzzBuzz(10, "buzz")

def test_returnfizzbuzzwith15Passedin():
    checkFuzzBuzz(15, "fizzbuzz")
