from utils.composition import composeif

class TestComposeIf:
    def test_shouldBe_identity_when_emptyList(self):
        assert 1 == composeif([])(1)

    def test_shouldBe_identity_when_listWithAllFalse(self):
        assert 1 == composeif([(False, lambda x: x - 1), (False, lambda x: x * 2)])(1)

    def test_shouldBe_allFunctions_when_listWithAllTrue(self):
        assert 3 == composeif([(True, lambda x: x - 1), (True, lambda x: x * 2)])(2)

    def test_shouldBe_justTrueFunctions_when_listWithSomeTrue(self):
        assert 4 == composeif([(False, lambda x: x - 1), (True, lambda x: x * 2)])(2)