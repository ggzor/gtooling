import pytest
from utils.string import isempty

@pytest.mark.parametrize("value, expected", [
    ("", True),
    ("   ", True),
    ("a", False)
])
def test_shouldBe_expected_when_valueIs(value, expected):
    assert expected == isempty(value)