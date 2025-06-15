from app.generator import generate_questions

def test_generate_questions_basic():
    brand = "Nike"
    product = "shoes"
    questions = generate_questions(brand, product)
    assert isinstance(questions, list)
    assert len(questions) >= 5
    assert all(brand.lower() in q.lower() or product.lower() in q.lower() for q in questions)