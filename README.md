# RoboBill 💪

RoboBill is a small Streamlit app that reads a photo of a bill, receipt or invoice and uses Google's Gemini model to turn it into a short expense report.

Upload an image, ask a question about it (for example "Summarize this bill and tell me the total"), and RoboBill returns:

1. Store or business name
2. Date of purchase
3. Total amount spent
4. List of purchased items
5. Expense summary
6. Feedback or suggestions on the spending

## Tech stack

- [Streamlit](https://streamlit.io/) for the web UI
- [Google Gemini](https://ai.google.dev/) (`gemini-flash-latest`) through the `google-generativeai` SDK for multimodal image + text understanding
- Pillow for image handling
- python-dotenv for local configuration

## Getting started

Requires Python 3.9 or newer.

```bash
git clone https://github.com/OjalSingh/RoboBill-using-Gemini-API.git
cd RoboBill-using-Gemini-API

python -m venv .venv
source .venv/bin/activate      # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Add your API key

1. Create a free Gemini API key at [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Copy the example env file and paste your key into it:

   ```bash
   cp .env.example .env
   ```

   ```
   GOOGLE_API_KEY=your-gemini-api-key-here
   ```

`.env` is listed in `.gitignore`, so your key stays on your machine. Never commit it.

### Run the app

```bash
streamlit run app.py
```

Streamlit opens the app at http://localhost:8501.

## How it works

`app.py` reads the uploaded image as bytes and sends it to Gemini together with a fixed system prompt (describing the report format) and your own question. Gemini's text answer is shown under "Result of Analysis".

## Project structure

```
app.py            Streamlit app and Gemini call
requirements.txt  Python dependencies
.env.example      Template for your local .env
```
