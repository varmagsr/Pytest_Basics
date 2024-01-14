import pytest
from _pytest.python_api import approx
## mostly float values like 0.1+0.2  will not match with 0.3 as sumation will
## give you the long dicimel vale with diffrent number in the end
## So use approx() funcation to macth or assert the floating numbers.
def test_floatAssert():
    assert (0.1 + 0.2) == approx(0.3)
