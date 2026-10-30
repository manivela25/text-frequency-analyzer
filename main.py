from src.analyzer import TextAnalyzer
from src.cleaner import TextCleaner
from src.visualizer import ConsoleVisualizer


def main():
    # 1. Read input file
    with open("data/sample.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()

    # 2. Clean and tokenize
    cleaner = TextCleaner(stopwords_file="data/stopwords.txt")
    clean_words = cleaner.get_clean_words(raw_text)

    # 3. Analyze frequencies
    analyzer = TextAnalyzer(clean_words)
    top_words = analyzer.get_most_common(top_n=5)

    # 4. Render terminal chart
    visualizer = ConsoleVisualizer()
    visualizer.draw_chart(top_words)


if __name__ == "__main__":
    main()
