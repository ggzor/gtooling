import pytest

from utils.arguments.types import spacing

from utils.arguments.converters import equals_to
from utils.arguments.converters.numerics import positive_integer, to_integer
from utils.arguments.converters.combination import choose_any

class TestChooseAny:
    @pytest.mark.parametrize("conversions, value, expected", [
        ([[positive_integer, to_integer], [equals_to(0), to_integer]], "0", 0),
        [[int, float], "0.5", 0.5]
    ])
    def test_shouldBe_expected_when_conversionsAre_and_valueIs(self, conversions, value, expected):
        assert expected == choose_any(conversions)(value)

    def test_should_throwException_when_noConversionSucceeds(self):
        space = " " * spacing * 2
        message = """There were exceptions trying to parse the value '0.5':
{}- The value '0.5' is not a valid integer.
{}- The value '0.5' is not a valid integer.""".format(space, space)
        with pytest.raises(Exception, match=message):
            choose_any([to_integer, to_integer])('0.5')