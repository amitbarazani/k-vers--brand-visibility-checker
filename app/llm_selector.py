# app/decorators.py
import os
from functools import wraps

def use_llm(func):
    if os.getenv("OPENAI_API_KEY"):
        from .llm_client import get_llm_answers
        source = "OpenAI API"
    else:
        from .mock_llm_client import get_llm_answers
        source = "Mock Client"

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, get_llm_answers=get_llm_answers, llm_source=source, **kwargs)

    return wrapper
