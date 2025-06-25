import os
import sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)  # noqa: E402

from OHNLP.wordsngram.wordsngram import wordsngram  # noqa: E402


class TestWordsNgram(unittest.TestCase):
    def test_unigram_single_word(self):
        result = wordsngram("Hi.", n=1, mode="front")
        expected = {("Hi",): 0.5, (".",): 0.5}
        self.assertEqual(result, expected)

    def test_bigram_front_abbrev(self):
        text = "Hello, U.S.A. world."
        result = wordsngram(text, n=2, mode="front")
        expected = [
            ("Hello", ","),
            (",", "U.S.A."),
            ("U.S.A.", "world"),
            ("world", "."),
        ]
        self.assertEqual(set(result.keys()), set(expected))
        for freq in result.values():
            self.assertAlmostEqual(freq, 1 / 4)

    def test_bigram_back_abbrev(self):
        text = "Hello, U.S.A. world."
        result = wordsngram(text, n=2, mode="back")
        expected = [
            (".", "world"),
            ("world", "U.S.A."),
            ("U.S.A.", ","),
            (",", "Hello"),
        ]
        self.assertEqual(set(result.keys()), set(expected))

    def test_trigram_window(self):
        result = wordsngram("Hi there", n=3, mode="window")
        expected = [
            ("<s>", "<s>", "Hi"),
            ("<s>", "Hi", "there"),
            ("Hi", "there", "</s>"),
            ("there", "</s>", "</s>"),
        ]
        self.assertEqual(set(result.keys()), set(expected))
        for freq in result.values():
            self.assertAlmostEqual(freq, 1 / 4)

    def test_long_phrase(self):
        words = [f"w{i}" for i in range(1, 21)]
        text = " ".join(words[:2]) + ", " + " ".join(words[2:]) + "."
        result = wordsngram(text, n=1, mode="front")
        expected_tokens = [(w,) for w in words + [",", "."]]
        self.assertEqual(set(result.keys()), set(expected_tokens))
        for freq in result.values():
            self.assertAlmostEqual(freq, 1 / 22)


if __name__ == "__main__":
    unittest.main()
