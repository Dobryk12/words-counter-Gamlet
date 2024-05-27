# words-counter-Gamlet

This Python script parses all words from the book "Hamlet" and records their frequency of occurrence in a CSV file.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Description

This project aims to analyze the frequency of words in the famous play "Hamlet" by William Shakespeare. It uses web scraping techniques to extract the text of the play from a website and then counts the occurrence of each word. The results are saved in a CSV file for further analysis.

## Features

- Parses the text of "Hamlet" from a website
- Removes punctuation and digits from the text
- Counts the frequency of each word
- Saves the word counts in a CSV file

## Installation

1. Clone the repository: 
```bash
git clone https://github.com/Dobryk12/words-counter-Gamlet.git
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Python script `word_count_hamlet.py`

2. After the script finishes executing, you will find a file named `word_counts.csv` in the project directory. This file contains the word counts in CSV format.