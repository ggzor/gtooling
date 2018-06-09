from utils.string import multiline_to_singleline

expected = "Multiline to single line"

class TestMultilineToSingleLine:
    def test_shouldBe_empty_when_empty(self):
        assert "" == multiline_to_singleline("")

    def test_shouldBe_oneline_when_multiline_and_defaultParameters(self):
        st = """Multiline
to
single
line"""

        assert expected == multiline_to_singleline(st)

    def test_shouldBe_oneline_when_multiline_and_leadingAndTrailingWhitespaces_and_stripped(self):
        st = """
            Multiline
            to
            single
            line"""
        
        assert expected == multiline_to_singleline(st, strip=True, remove_emptylines=True)