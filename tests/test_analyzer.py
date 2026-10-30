import unittest
from src.cleaner import TextCleaner
from src.analyzer import TextAnalyzer


class TestTextCleaner(unittest.TestCase):
    def setUp(self):
        # Her testten önce temizleyici sınıfı başlatılır
        self.cleaner = TextCleaner(stopwords_file="data/stopwords.txt")

    def test_remove_punctuation(self):
        # Noktalama işaretlerinin temizlendiğini doğrula
        dirty_text = "hello, world! python... is? great:"
        clean_text = self.cleaner.remove_punctuation(dirty_text)
        self.assertEqual(clean_text, "hello world python is great")

    def test_get_clean_words_filters_stopwords(self):
        # Durak kelimelerin ve büyük harflerin ayıklandığını doğrula
        text = "Python is fun and python is powerful."
        words = self.cleaner.get_clean_words(text)
        
        # 'is' ve 'and' stopwords.txt içinde olduğu için listede olmamalı
        self.assertNotIn("is", words)
        self.assertNotIn("and", words)
        # 'Python' küçük harfe dönmüş olmalı
        self.assertIn("python", words)


class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        # Örnek temiz kelime listesi
        self.sample_words = ["code", "python", "code", "readable", "code"]
        self.analyzer = TextAnalyzer(self.sample_words)

    def test_count_frequencies(self):
        # Kelime frekans sayılarının doğruluğunu test et
        frequencies = self.analyzer.count_frequencies()
        self.assertEqual(frequencies["code"], 3)
        self.assertEqual(frequencies["python"], 1)
        self.assertEqual(frequencies["readable"], 1)

    def test_get_most_common_order(self):
        # En çok geçen kelimelerin sıralamasını test et
        top_words = self.analyzer.get_most_common(top_n=2)
        # İlk sırada en çok geçen ('code', 3) olmalı
        self.assertEqual(top_words[0], ("code", 3))
        # Toplamda 2 eleman dönmeli
        self.assertEqual(len(top_words), 2)


if __name__ == "__main__":
    unittest.main()
