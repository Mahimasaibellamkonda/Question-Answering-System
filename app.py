from flask import Flask, render_template, request
import re

app = Flask(__name__)


def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def tokenize(text):
    return set(
        re.findall(r'\b[a-zA-Z]{2,}\b', text.lower())
    )


def find_answer(question, context):
    question_words = tokenize(question)
    sentences = split_sentences(context)

    if not sentences:
        return "No answer could be found."

    stop_words = {
        "what", "where", "when", "who", "why", "how",
        "is", "are", "was", "were", "the", "a", "an",
        "of", "to", "in", "on", "for", "and", "or",
        "does", "do", "did", "can", "could", "which"
    }

    question_keywords = question_words - stop_words

    best_sentence = None
    best_score = 0

    for sentence in sentences:
        sentence_words = tokenize(sentence)

        matching_words = question_keywords.intersection(
            sentence_words
        )

        score = len(matching_words)

        if score > best_score:
            best_score = score
            best_sentence = sentence

    if best_sentence and best_score > 0:
        return best_sentence

    return "No relevant answer was found in the provided context."


@app.route("/", methods=["GET", "POST"])
def index():
    context = ""
    question = ""
    answer = ""

    if request.method == "POST":
        context = request.form.get("context", "").strip()
        question = request.form.get("question", "").strip()

        if context and question:
            answer = find_answer(question, context)

    return render_template(
        "index.html",
        context=context,
        question=question,
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)
