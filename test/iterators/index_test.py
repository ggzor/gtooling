from utils.iterators import index

class TestIndex:
    def test_shouldBe_empty_when_empty(self):
        assert [] == list(index([]))

    def test_shouldBe_zippedWithIndex_when_nonEmpty(self):
        assert [(0, "a"), (1, "b")] == list(index("ab"))

    def test_shouldBe_zippedWithIndexAndOffset_when_nonEmptyAndOffset(self):
        assert [(1, "a"), (2, "b")] == list(index("ab", start=1))