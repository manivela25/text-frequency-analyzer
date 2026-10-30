class TextCleaner:
    def __init__(self, stopwords_file: str = "data/stopwords.txt"):
        # Temizlemek istediğimiz noktalama işaretleri
        self.punctuation = ".,!?;:-"
        # Durak kelimeleri dosyadan küme (set) olarak yüklüyoruz
        self.stopwords = self.load_stopwords(stopwords_file)

    def load_stopwords(self, file_path: str) -> set:
        """Dosyadaki durak kelimeleri okuyup bir küme (set) yapar."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                words = set()
                for line in file:
                    word = line.strip().lower()
                    if word:
                        words.add(word)
                return words
        except FileNotFoundError:
            return set()

    def remove_punctuation(self, text: str) -> str:
        """Metindeki noktalama işaretlerini siler."""
        clean_text = text
        for char in self.punctuation:
            clean_text = clean_text.replace(char, "")
        return clean_text

    def get_clean_words(self, text: str) -> list:
        """Metni küçük harfe çevirir, noktalamaları siler ve durak kelimeleri eler."""
        # 1. Küçük harfe çevir
        lower_text = text.lower()

        # 2. Noktalamaları temizle
        text_without_punct = self.remove_punctuation(lower_text)

        # 3. Boşluklardan bölüp kelime listesi yap
        all_words = text_without_punct.split()

        # 4. Durak kelimeleri (stopwords) listeden çıkar
        filtered_words = []
        for word in all_words:
            if word not in self.stopwords:
                filtered_words.append(word)

        return filtered_words
