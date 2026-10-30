# Text Frequency Analyzer

A modular, zero-dependency Python utility designed to sanitize, analyze, and visualize word frequency distributions from
raw text files. Built as the practical portfolio project for **Course 1: Crash Course on Python (Google IT Automation
with Python)**.

## Key Features

- **Punctuation & Stop-Word Filtering:** Normalizes text case, removes punctuation, and filters common stop words loaded
  from an external file (`data/stopwords.txt`).
- **Statistical Aggregation:** Computes raw frequency counts using native Python dictionaries and ranks them in
  descending order.
- **Terminal Data Visualization:** Renders an aligned, pure ASCII horizontal bar chart directly in the console without
  third-party plotting libraries.
- **Unit Tested:** Includes unit tests using Python's built-in `unittest` framework to ensure logic reliability.

## Architecture & Design

The project strictly follows Object-Oriented Programming (OOP) and Single Responsibility principles:

- `src/cleaner.py` (`TextCleaner`): Sanitizes strings, strips punctuation, and extracts non-stop-word tokens.
- `src/analyzer.py` (`TextAnalyzer`): Calculates frequency distributions and identifies top-N occurrences.
- `src/visualizer.py` (`ConsoleVisualizer`): Draws formatted ASCII bar charts to stdout.
- `main.py`: Coordinates the end-to-end pipeline from file reading to console visualization.

## Project Structure

```text
text-frequency-analyzer/
├── data/
│   ├── sample.txt          # Sample input text
│   └── stopwords.txt       # Common words to filter out
├── src/
│   ├── __init__.py
│   ├── analyzer.py         # Frequency counting and ranking
│   ├── cleaner.py          # Text sanitization and tokenization
│   └── visualizer.py       # Console ASCII chart renderer
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py    # Unit tests for cleaner and analyzer
├── main.py                 # Pipeline execution entry point
├── .gitignore
└── README.md

Getting Started
Prerequisites
Python 3.8 or higher (No third-party packages required).

Installation & Execution
Clone the repository:

Bash
git clone [https://github.com/manivela25/text-frequency-analyzer.git](https://github.com/manivela25/text-frequency-analyzer.git)
cd text-frequency-analyzer
Run the main application:

Bash
python3 main.py
Run the automated unit tests:

Bash
python3 -m unittest tests/test_analyzer.py -v
Example Output
Plaintext
========================================
📊 WORD FREQUENCY DISTRIBUTION
========================================
code         | ████ (4)
python       | ███ (3)
readable     | ██ (2)
fun          | █ (1)
powerful     | █ (1)
========================================
Course Alignment
This project satisfies the core competencies taught in Google's Crash Course on Python:

String manipulation and string methods

Collections and data structures (list, dict, set, tuple)

File I/O operations with context managers (with open(...))

Object-Oriented Programming (Classes, methods, separation of concerns)

Unit testing with unittest