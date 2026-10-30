class TextCleaner:
    def __init__(self, stopwords_file: str = "data/stopwords.txt"):
        """Initializes cleaner with target punctuation and stop words."""
        self.punctuation = ".,!?;:-"
        self.stopwords = self.load_stopwords(stopwords_file)

    def load_stopwords(self, file_path: str) -> set:
        """Loads stop words from an external file into a set."""
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
        """Removes defined punctuation characters from the input text."""
        clean_text = text
        for char in self.punctuation:
            clean_text = clean_text.replace(char, "")
        return clean_text

    def get_clean_words(self, text: str) -> list:
        """Converts text to lowercase, removes punctuation, and filters stop words."""
        lower_text = text.lower()
        text_without_punct = self.remove_punctuation(lower_text)
        all_words = text_without_punct.split()

        filtered_words = []
        for word in all_words:
            if word not in self.stopwords:
                filtered_words.append(word)

        return filtered_words
