class TextAnalyzer:
    def __init__(self, words: list):
        # Temizlenmiş kelime listesini saklıyoruz
        self.words = words

    def count_frequencies(self) -> dict:
        """Kelimelerin metinde kaçar kez geçtiğini bir sözlükte (dict) sayar."""
        counts = {}
        for word in self.words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts

    def get_most_common(self, top_n: int = 5) -> list:
        """En çok tekrar eden ilk N kelimeyi çoktan aza sıralı olarak döndürür."""
        frequencies = self.count_frequencies()
        
        # Sözlüğü değerlerine (sayılarına) göre büyükten küçüğe sıralıyoruz
        sorted_words = sorted(
            frequencies.items(), 
            key=lambda item: item[1], 
            reverse=True
        )
        
        return sorted_words[:top_n]
