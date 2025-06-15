# Brand Visibility Checker

This is a demo project that analyzes public visibility and sentiment for a given brand and product,
with optional integration to OpenAI’s GPT models or a mock fallback.

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python run.py
   ```

## 🔍 Features

- Analyze sentiment from generated answers
- Extract competitor brands
- Mock support for LLM (if no OpenAI key provided)
- Supports Flask-based web UI

## 🧪 Running Tests

To run the unit tests:

```bash
pytest
```

## ✅ Continuous Integration

This project includes a basic GitHub Actions workflow that automatically runs tests on each push.

- Location: `.github/workflows/tests.yml`
- Trigger: `push` to any branch
- Action: Installs dependencies and runs `pytest`
