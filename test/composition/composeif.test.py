from unittest import TestCase, main
from utils.composition import composeif

class ComposeIfTests(TestCase):
    def test_shouldBe_identity_when_emptyList(self):
        self.assertEqual(1, composeif([])(1))

    def test_shouldBe_identity_when_listWithAllFalse(self):
        self.assertEqual(1, composeif([(False, lambda x: x - 1), (False, lambda x: x * 2)])(1))

    def test_shouldBe_allFunctions_when_listWithAllTrue(self):
        self.assertEqual(3, composeif([(True, lambda x: x - 1), (True, lambda x: x * 2)])(2))

    def test_shouldBe_justTrueFunctions_when_listWithSomeTrue(self):
        self.assertEqual(4, composeif([(False, lambda x: x - 1), (True, lambda x: x * 2)])(2))

main()