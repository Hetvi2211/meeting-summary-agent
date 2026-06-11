import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
import google.generativeai as genai

from database import save_to_db, get_all_summaries

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Flask App
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    summary = ""
    transcript = ""

    if request.method == "POST":

        transcript = request.form.get("transcript", "")

        prompt = f"""
You are a meeting assistant.

Analyze this meeting transcript.

Provide:

1. Meeting Summary
2. Action Items
3. Owners

Transcript:

{transcript}
"""

        try:
            response = model.generate_content(prompt)
            summary = response.text

            save_to_db(summary)

        except Exception as e:
            summary = f"Error: {str(e)}"

    return render_template(
        "index.html",
        summary=summary,
        transcript=transcript
    )


@app.route("/history")
def history():

    summaries = get_all_summaries()

    return render_template(
        "history.html",
        summaries=summaries
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )