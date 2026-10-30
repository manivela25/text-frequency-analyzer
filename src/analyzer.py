class TextAnalyzer:
    def __init__(self, words: list):
        """Initializes analyzer with a list of clean tokens."""
        self.words = words

    def count_frequencies(self) -> dict:
        """Counts occurrences of each word and returns a dictionary."""
        counts = {}
        for word in self.words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts

    def get_most_common(self, top_n: int = 5) -> list:
        """Returns the top N most frequent words in descending order."""
        frequencies = self.count_frequencies()
        sorted_words = sorted(
            frequencies.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return sorted_words[:top_n]
