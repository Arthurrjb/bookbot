# Bookbot

A command-line text analysis tool built in Python that reads a book file and generates a report with word counts and character frequency statistics.

## Overview

Bookbot is a beginner-friendly Python project focused on core programming fundamentals such as file I/O, dictionaries, functions, sorting, and command-line arguments. Given the path to a `.txt` file, the program analyzes the text and prints a formatted summary to the terminal.

## Features

- Reads book text from a file
- Accepts the file path as a command-line argument
- Counts total words in the document
- Counts occurrences of each character
- Sorts and displays character frequency results
- Produces a clean terminal report

## Example Usage

```bash
python3 main.py books/frankenstein.txt
```

## Example Output
```bash
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
a: 26743
b: 4868
c: 9011
...
============= END ===============
```

## Project Structure

```bash
.
├── main.py
├── stats.py
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
└── README.md
```

## How It Works
main.py handles command-line input and prints the report
stats.py contains the logic for:
- counting words
- counting characters
- sorting character data

## Requirements
Python 3

## Run the Project
Clone the repository
Navigate into the project folder
Run:
```bash
python3 main.py books/frankenstein.txt
```

## What This Project Demonstrates
- Writing modular Python code
- Working with text files and file paths
- Parsing and analyzing text data
- Using dictionaries for frequency counting
- Sorting structured data for reporting
- Building simple CLI applications

## Possible Improvements
- Ignore uppercase/lowercase differences more explicitly
- Filter out non-letter characters
- Export results to a file
- Add tests

## About
This project was built as part of a Boot.dev backend learning project and serves as a practical introduction to building command-line tools in Python.

## License
This project is for learning purposes.