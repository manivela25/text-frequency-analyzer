# Text Frequency Analyzer

A modular, zero-dependency Python tool designed to sanitize, analyze, and visualize word frequency distributions from raw text files. Built as the capstone project for **Course 1: Crash Course on Python (Google IT Automation with Python)**.

## Overview

The engine processes raw text inputs through an object-oriented architecture:
1. **Sanitization (`cleaner.py`):** Normalizes text case, removes punctuation, and filters common stop words loaded from an external dictionary (`stopwords.txt`).
2. **Frequency Analysis (`analyzer.py`):** Uses dictionary-based aggregation to calculate word occurrences and orders them by frequency using lambda sorting.
3. **Visualization (`visualizer.py`):** Renders the distribution as an aligned ASCII bar chart directly in the terminal without external plotting libraries.

## Directory Structure

```text
text-frequency-analyzer/
├── data/
│   ├── sample.txt          # Sample input text
│   └── stopwords.txt       # Excluded common words
├── src/
│   ├── cleaner.py          # Text cleaning and token filtering
│   ├── analyzer.py         # Frequency counting and ranking
│   └── visualizer.py       # Terminal ASCII chart renderer
├── tests/
│   └── test_analyzer.py    # Unit tests using Python's unittest module
├── main.py                 # Pipeline execution entry point
└── README.md

Getting Started
Prerequisites
Python 3.8+ (No external packages required).

Usage
Clone the repository and navigate to the folder:

Bash
git clone [https://github.com/](https://github.com/)<your-username>/text-frequency-analyzer.git
cd text-frequency-analyzer
Run the analyzer:

Bash
python3 main.py
Run the unit tests:

Bash
python3 -m unittest tests/test_analyzer.py -v
Example Output
Plaintext
========================================
📊 KELİME FREKANS GRAFİĞİ
========================================
code         | ████ (4)
python       | ███ (3)
readable     | ██ (2)
fun          | █ (1)
powerful     | █ (1)
========================================



