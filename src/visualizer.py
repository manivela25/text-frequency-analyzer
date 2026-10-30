class ConsoleVisualizer:
    def __init__(self, char: str = "█"):
        # Çubukları çizerken kullanacağımız karakter
        self.char = char

    def draw_chart(self, word_tuples: list) -> None:
        """Kelimeleri ve frekanslarını çubuk grafik olarak konsola basar."""
        if not word_tuples:
            print("Görselleştirilecek veri yok.")
            return

        print("\n" + "=" * 40)
        print("📊 KELİME FREKANS GRAFİĞİ")
        print("=" * 40)

        for word, count in word_tuples:
            # Sayı kadar karakteri yan yana koyuyoruz
            bar = self.char * count
            # Kelimeyi sola yaslayıp yanına çubuğu ve sayıyı yazıyoruz
            print(f"{word:<12} | {bar} ({count})")

        print("=" * 40 + "\n")
