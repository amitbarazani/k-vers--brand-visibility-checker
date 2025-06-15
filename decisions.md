# Architectural and Technical Decisions

## 1. Language & Framework

**Decision:** Python with Flask

**Reasoning:**

- Simple for prototyping
- Easy integration with OpenAI
- Lightweight deployment

## 2. Project Structure

**Decision:** Use modular structure (`app/` folder with `routes`, `llm_client`, `analyzer`, etc.)

**Reasoning:**

- Keeps concerns separated
- Easier to mock LLM logic

## 3. LLM Fallback

**Decision:** Mock client used when `OPENAI_API_KEY` not set.

**Reasoning:**

- Allows offline dev and testing
- Avoids quota/latency in demo mode

## 4. Decorator for LLM Choice

**Decision:** Use a decorator to inject real or mock `get_llm_answers` based on ENV.

**Reasoning:**

- Clean dependency injection
- Makes testability simple

## 5. Sentiment Analysis

**Decision:** Use `textblob` for basic sentiment scoring

**Reasoning:**

- Simple API
- Good enough for demo-level NLP

## 6. Dockerization

**Decision:** Provide `Dockerfile` to support consistent environments

**Reasoning:**

- Easy deployment on local/remote
- Simplifies dependencies

## 7. Mock Mode Default

**Decision:** If `OPENAI_API_KEY` is missing, fallback to mock.

**Reasoning:**

- Ensures the app still works with no key

## 8. CI with GitHub Actions

**Decision:** A lightweight GitHub Actions workflow was added to automatically run `pytest` on push.

**Reasoning:**

- Ensures test integrity with every change.
- Helps demonstrate production-readiness in a simple way.
- Lightweight and runs within GitHub’s free-tier limits.

### Development Time

- The entire task was completed in approximately **2.5 hours**, including development, testing, and deployment.
