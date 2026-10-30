from src.cleaner import TextCleaner
from src.analyzer import TextAnalyzer
from src.visualizer import ConsoleVisualizer

def main():
    # 1. Metni oku
    with open("data/sample.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()

    # 2. Temizle
    cleaner = TextCleaner(stopwords_file="data/stopwords.txt")
    clean_words = cleaner.get_clean_words(raw_text)

    # 3. Analiz Et
    analyzer = TextAnalyzer(clean_words)
    top_words = analyzer.get_most_common(top_n=5)

    # 4. Görselleştir
    visualizer = ConsoleVisualizer()
    visualizer.draw_chart(top_words)

if __name__ == "__main__":
    main()
