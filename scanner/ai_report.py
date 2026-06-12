import os
import importlib

try:
    genai = importlib.import_module("google.generativeai")
except ImportError as e:
    raise ImportError(
        "google.generativeai package is required. Install with `pip install google-generativeai`."
    ) from e

try:
    st = importlib.import_module("streamlit")
except ImportError:
    st = None

if st is not None:
    gemini_api_key = st.secrets.get("GEMINI_API_KEY")
else:
    gemini_api_key = None

if not gemini_api_key:
    gemini_api_key = os.environ.get("GEMINI_API_KEY")

if not gemini_api_key:
    raise RuntimeError("GEMINI_API_KEY must be set in Streamlit secrets or environment variables.")

genai.configure(
    api_key=gemini_api_key
)

@st.cache_data
def generate_recommendations(
    headers,
    ssl_info,
    technologies,
    ports
):

    try:

        model = genai.GenerativeModel(
            "gemini-flash-latest"
        )

        prompt = f"""
You are a professional cybersecurity analyst.

Analyze these scan results.

Provide:

1. Security Summary
2. Risk Assessment
3. Recommendations

Headers:
{headers}

SSL:
{ssl_info}

Technologies:
{technologies}

Ports:
{ports}

Keep the response concise.
"""

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"AI Analysis Error: {str(e)}"