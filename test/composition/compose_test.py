from utils.composition import compose

class TestCompose:
    def test_shouldBe_emptyList_when_emptyList(self):
        assert 1 == compose([])(1)

    def test_shouldBe_sameFunction_when_singleFunction(self):
        assert 4 == compose([lambda x: x * 2])(2)

    def test_shouldBe_compositionOfFunctions_when_multipleFunctions(self):
        assert 7 == compose([(lambda x: x - 1), (lambda x: x * 4)])(2)