# Question Answering System

A web-based Text and Speech Analysis application that finds relevant answers from a given text context based on a user's question.

## Features

* Accepts a document or paragraph as context
* Accepts natural-language questions
* Extracts important words from the question
* Compares question keywords with sentences in the context
* Finds the most relevant sentence
* Displays the answer through a web interface
* Simple and responsive design

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* Regular Expressions
* Basic Natural Language Processing

## Project Structure

```text
Question-Answering-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

Open a terminal inside the project folder and install the required package:

```bash
pip install -r requirements.txt
```

## Running the Application

Run:

```bash
python app.py
```

The application will start at:

```text
http://127.0.0.1:5000
```

Open the address in a web browser.

## How It Works

1. The user provides a context or document.
2. The user enters a question.
3. The question is converted into a set of important words.
4. The context is divided into individual sentences.
5. Each sentence is compared with the question keywords.
6. The sentence with the highest number of matching keywords is selected.
7. The selected sentence is displayed as the answer.

## Example

### Context

```text
Natural Language Processing is a branch of
Artificial Intelligence. It helps computers understand,
interpret, and generate human language.
```

### Question

```text
What is Natural Language Processing?
```

### Output

```text
Natural Language Processing is a branch of Artificial Intelligence.
```

## Applications

Question answering systems can be used in:

* Educational systems
* Document search
* Customer support
* Information retrieval
* FAQ systems
* Digital assistants
* Knowledge-based applications

## Advantages

* Simple to use
* Fast response
* Does not require a large database
* Works directly with user-provided context
* Demonstrates basic NLP-based question answering

## Limitations

This is a basic extractive question-answering system. It selects the most relevant sentence from the provided context rather than generating a completely new answer.

## Purpose

The project demonstrates how Natural Language Processing techniques can be applied to build a simple question-answering application using keyword matching and sentence-level relevance scoring.

## Author

B.E. CSE Student
