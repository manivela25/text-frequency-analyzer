class ConsoleVisualizer:
    def __init__(self, char: str = "█"):
        """Sets the character used for drawing the frequency bars."""
        self.char = char

    def draw_chart(self, word_tuples: list) -> None:
        """Renders word frequency distribution as an aligned ASCII bar chart."""
        if not word_tuples:
            print("No data available to visualize.")
            return

        print("\n" + "=" * 40)
        print("📊 WORD FREQUENCY DISTRIBUTION")
        print("=" * 40)

        for word, count in word_tuples:
            bar = self.char * count
            print(f"{word:<12} | {bar} ({count})")

        print("=" * 40 + "\n")
