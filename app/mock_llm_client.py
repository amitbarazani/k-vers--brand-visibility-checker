
import os
from dotenv import load_dotenv
import random

load_dotenv()

# Simulate OpenAI client but return mock responses
def get_llm_answers(questions):
    mock_answers = [
        "Nike is often praised for its durability and brand reputation.",
        "Adidas and Puma are strong alternatives to Nike.",
        "Most customers are satisfied with Nike's performance shoes.",
        "Nike shoes are generally considered high quality.",
        "Compared to competitors, Nike invests heavily in innovation.",
        "Some users find Nike shoes slightly overpriced.",
        "Nike has strong market presence, especially in athletic footwear.",
        "Competitors like New Balance and Under Armour are frequently mentioned.",
        "Experts often recommend Nike for runners and athletes.",
        "The brand is known for combining performance and style."
    ]
    answers = []
    for q in questions:
        # Randomly choose an answer to simulate variation
        simulated_answer = random.choice(mock_answers)
        answers.append(simulated_answer)
    return answers
