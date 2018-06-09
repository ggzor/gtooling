import pytest
from utils.functional.composition import compose_monoid

and_function_identity = lambda x: True
and_function = lambda f, g: (lambda x: f(x) and g(x))

equals_five = lambda x: x == 5

class TestComposeMonoid:
    @pytest.mark.parametrize("identity, function", [
        (and_function_identity, and_function),
        ((lambda x: 0), lambda x, y: x + y)
    ])
    def test_shouldBe_identity_when_anyFunction_and_emptyList(self, identity, function):
        assert identity("any") == compose_monoid(identity, function)([])("any")

    @pytest.mark.parametrize("identity, function, singleFunction, value, expected", [
        (and_function_identity, and_function, equals_five, 5, True),
        (and_function_identity, and_function, equals_five, 4, False)
    ])
    def test_shouldBe_singleFunction_when_singleFunctionInList(self, identity, function, singleFunction, value, expected):
        assert expected == compose_monoid(identity, function)([singleFunction])(value)