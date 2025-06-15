# Brand Visibility Checker

This is a simple Flask-based web application that analyzes brand visibility and sentiment using AI or a mock service.

## Features

- Generate brand-related questions dynamically.
- Analyze brand visibility and sentiment from generated answers.
- Use either the OpenAI API or a local mock client.
- Clean and simple UI for interaction.

## Installation

```bash
git clone https://github.com/amitbarazani/k-vers--brand-visibility-checker.git
cd k-vers--brand-visibility-checker
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file based on `.env.example` and add your OpenAI key:

```
OPENAI_API_KEY=your_api_key_here
```

If no API key is provided, the app will use a mock client instead.

## Running the App

```bash
python run.py
```

The app will be available at `http://localhost:5000`.

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── analyzer.py
│   ├── generator.py
│   ├── llm_client.py
│   ├── mock_llm_client.py
│   ├── llm_selector.py
│   └── routes.py
├── templates
│   └── index.html
├── static
│   └── style.css
├── run.py
├── requirements.txt
└── .env.example
```

## Notes

- Uses `TextBlob` for sentiment analysis.
- Mock client provides fake answers for demo purposes.
- Includes logic to automatically choose between real and mock LLM.

---
