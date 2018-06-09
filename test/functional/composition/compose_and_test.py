import pytest 
from utils.functional.composition import compose_and

class TestComposeAnd:
    def test_shouldbe_true_when_emptyList(self):
        assert True == compose_and([])(4)

    @pytest.mark.parametrize("expected, value", [
        (True, 5),
        (False, -1)
    ])
    def test_shouldbe_singlefunction_when_singleFunctionInList(self, expected, value):
        assert expected == compose_and([lambda x: x > 0])(value)

    @pytest.mark.parametrize("expected, value", [
        (True, 3),
        (False, 5)
    ])
    def test_shouldbe_composition_when_multipleFunctionsInList(self, expected, value):
        assert expected == compose_and([(lambda x: x > 0), (lambda x: x < 4)])(value)