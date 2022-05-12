from n_grams import n_grams
import unittest


class NGramsTests(unittest.TestCase):
    def test_n_grams_one_word(self):
        self.assertEqual(n_grams("Show"), ["Show"])

    def test_n_grams_two_words(self):
        self.assertEqual(n_grams("Show me"), ["Show", "Show me", "me"])

    def test_n_grams_three_words(self):
        self.assertEqual(
            n_grams("Show me the"),
            [
                "Show",
                "Show me",
                "Show me the",
                "me",
                "me the",
                "the",
            ],
        )

    def test_n_grams_four_words(self):
        self.assertEqual(
            n_grams("Show me the code."),
            [
                "Show",
                "Show me",
                "Show me the",
                "Show me the code",
                "me",
                "me the",
                "me the code",
                "the",
                "the code",
                "code",
            ],
        )


if __name__ == "__main__":
    unittest.main()
