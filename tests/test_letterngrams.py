import os
import sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)  # noqa: E402

from OHNLP.letterngram.letterngram import letterngrams  # noqa: E402


class TestLetterNgrams(unittest.TestCase):
    def test_unigram_alpha(self):
        result = letterngrams("abc", num=1, charset="alpha")
        expected = {"a": 1 / 3, "b": 1 / 3, "c": 1 / 3}
        self.assertEqual(result, expected)

    def test_bigram_alpha(self):
        result = letterngrams("hi there", num=2, charset="alpha")
        expected_keys = {"hi", "th", "he", "er", "re"}
        self.assertEqual(set(result.keys()), expected_keys)
        for freq in result.values():
            self.assertAlmostEqual(freq, 1 / 5)


if __name__ == "__main__":
    unittest.main()
