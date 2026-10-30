import unittest

from src.analyzer import TextAnalyzer
from src.cleaner import TextCleaner


class TestTextCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = TextCleaner(stopwords_file="data/stopwords.txt")

    def test_remove_punctuation(self):
        dirty_text = "hello, world! python... is? great:"
        clean_text = self.cleaner.remove_punctuation(dirty_text)
        self.assertEqual(clean_text, "hello world python is great")

    def test_get_clean_words_filters_stopwords(self):
        text = "Python is fun and python is powerful."
        words = self.cleaner.get_clean_words(text)
        self.assertNotIn("is", words)
        self.assertNotIn("and", words)
        self.assertIn("python", words)


class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        self.sample_words = ["code", "python", "code", "readable", "code"]
        self.analyzer = TextAnalyzer(self.sample_words)

    def test_count_frequencies(self):
        frequencies = self.analyzer.count_frequencies()
        self.assertEqual(frequencies["code"], 3)
        self.assertEqual(frequencies["python"], 1)
        self.assertEqual(frequencies["readable"], 1)

    def test_get_most_common_order(self):
        top_words = self.analyzer.get_most_common(top_n=2)
        self.assertEqual(top_words[0], ("code", 3))
        self.assertEqual(len(top_words), 2)


if __name__ == "__main__":
    unittest.main()
