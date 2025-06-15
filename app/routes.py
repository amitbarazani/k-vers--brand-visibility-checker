from flask import Blueprint, render_template, request
from .generator import generate_questions
from .mock_llm_client import get_llm_answers
from .analyzer import analyze_answers
from .llm_selector import use_llm

main  = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
@use_llm
def index(get_llm_answers=None, llm_source=None):
    if request.method == "POST":
        brand = request.form["brand"]
        product = request.form["product"]

        questions = generate_questions(brand, product)
        answers = get_llm_answers(questions)
        analysis = analyze_answers(answers, brand)

        return render_template("index.html",
                               brand=brand,
                               product=product,
                               questions=questions,
                               answers=answers,
                               analysis=analysis,
                               zip=zip,
                               llm_source=llm_source)

    return render_template("index.html")



