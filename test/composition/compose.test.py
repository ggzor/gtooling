from unittest import TestCase, main
from utils.composition import compose

class ComposeTests(TestCase):
    def test_shouldBe_emptyList_when_emptyList(self):
        self.assertEqual(1, compose([])(1))

    def test_shouldBe_sameFunction_when_singleFunction(self):
        self.assertEqual(4, compose([lambda x: x * 2])(2))

    def test_shouldBe_compositionOfFunctions_when_multipleFunctions(self):
        self.assertEqual(7, compose([(lambda x: x - 1), (lambda x: x * 4)])(2))

main()