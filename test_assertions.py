import pytest

def test_IntAssert():
    assert 1 == 1

def test_StrAssert():
    assert "str" == "str"

def test_FloatAssert():
    assert 1.0 == 1.0

def test_arrayAssert():
    assert [1, 2, 3] == [1, 2, 3]

def test_dicAssert():
    assert {"1", 1} == {"1", 1}

