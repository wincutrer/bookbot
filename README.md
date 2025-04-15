# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a command-line tool that analyzes classic books and prints a word and character frequency report, sorted from most to least frequent. It's a great way to dive into text processing with Python!

---

## Features

- Reads full-text books from plain `.txt` files
- Counts total words
- Counts character frequency (case-insensitive)
- Filters out non-alphabet characters for clean reports
- Sorts characters from most to least common
- CLI support — pass any `.txt` file path as input

---

## How to Run

```bash
python3 main.py <path_to_book>
```

## Example
```bash
python3 main.py books/frankenstein.txt
```

## Learnings

This project helped reinforce:

- Looping through strings and dictionaries

- Character vs. word handling

- Filtering and sorting data

- Structuring a real CLI tool
