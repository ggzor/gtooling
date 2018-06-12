import pytest
from utils.arguments.converters.numerics import to_integer, positive_integer, positive_integer_or_zero

class TestInteger:
    def test_shouldBe_expected_when_valueIs(self):
        assert 1 == to_integer("1")

    def test_should_throwException_when_valueIs(self):
        with pytest.raises(Exception, match="The value 'a' is not a valid integer."):
            to_integer("a")

class TestPositiveInteger:
    def test_shouldBe_sameValue_when_valueIsPositive(self):
        assert 1 == positive_integer(1)

    def test_should_throwException_when_valueIsNotPositive(self):
        with pytest.raises(Exception, match="The value -2 is not positive."):
            positive_integer(-2)

class TestPositiveIntegerOrZero:
    @pytest.mark.parametrize("value", [
        0, 5
    ])
    def test_shouldBe_sameValue_when_valueIsPositiveOrZero(self, value):
        assert value == positive_integer_or_zero(value)

    def test_should_throwException_when_valueIsNegative(self):
        with pytest.raises(Exception, match="The value -1 is not positive."):
            positive_integer_or_zero(-1)