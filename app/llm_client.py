import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

def get_llm_answers(questions):
    answers = []
    for question in questions:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
            )
            answers.append(response.choices[0].message.content.strip())
        except Exception as e:
            answers.append(f"[Error generating answer: {str(e)}]")
    return answers