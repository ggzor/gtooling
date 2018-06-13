import pytest
from utils.arguments.converters import equals_to

def test_shouldBe_value_when_valueIsSameThatParameter():
    assert 0 == equals_to(0)(0)

def test_should_throwException_when_valueIsDistinctToParameter():
    with pytest.raises(Exception, match="The value '0' is not equal to 1."):
        equals_to(1)(0)