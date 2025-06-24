import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import unittest
from unittest import mock

import OHNLP.letterngram.letterngram as ln
from OHNLP.langdetector.langdetector import language_detection

LANGUAGE_SAMPLES = [
    ("english", "hello"),
    ("mandarin", "ni hao"),
    ("hindi", "namaste mere dost"),
    ("spanish", "hola mi buen amigo"),
    ("arabic", "marhaban kayfa halak ya sadiqi"),
    ("bengali", "halo amar priyo bandhu kamon acho"),
    ("french", "bonjour mon cher ami comment allez vous"),
    ("russian", "privet moy dorogoy drug kak ty segodnya"),
    ("portuguese", "ola meu querido amigo como voce esta hoje"),
    ("urdu", "salam mere pyare dost aap kaise hain aaj sab theek"),
]


def _make_models():
    models = {}
    for lang, sample in LANGUAGE_SAMPLES:
        models[lang] = ln.letterngrams(sample, num=2, charset="alpha")
    return models


class TestLanguageDetection(unittest.TestCase):
    def setUp(self):
        self.patcher = mock.patch(
            "OHNLP.langdetector.langdetector.readmodels",
            return_value=_make_models(),
        )
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_detection(self):
        for lang, sample in LANGUAGE_SAMPLES:
            with self.subTest(language=lang):
                self.assertEqual(language_detection(sample), lang)


if __name__ == "__main__":
    unittest.main()
