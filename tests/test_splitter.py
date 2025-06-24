import os
import sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)  # noqa: E402

from OHNLP.splitter.splitter import splitter  # noqa: E402


class TestSplitter(unittest.TestCase):
    def test_abbreviations(self):
        text = (
            "Mr. John met Mrs. Jane at St. Patrick's Cathedral. "
            "They talked with Dr. Smith."
        )
        expected = [
            "Mr. John met Mrs. Jane at St. Patrick's Cathedral.",
            "They talked with Dr. Smith.",
        ]
        self.assertEqual(splitter(text), expected)

    def test_multiline(self):
        text = "Hello world!\nHow are you today? I am fine."
        expected = ["Hello world!", "How are you today?", "I am fine."]
        self.assertEqual(splitter(text), expected)

    def test_complex(self):
        text = "Dr. Strange loves the U.S.A. He said hi."
        expected = ["Dr. Strange loves the U.S.A. He said hi."]
        self.assertEqual(splitter(text), expected)


if __name__ == "__main__":
    unittest.main()
