from unittest.mock import patch
from ai_toolkit import sentiment, summarize, translate



def test_summarize():
    with patch("ai_toolkit.call_gemini") as mock:
        mock.return_value = "FAKE SUMMARY"
        result = summarize("Python is useful.")
        mock.assert_called_once_with(
    "Summarize the following text concisely. Return only the summary. Do not add phrases like \"Here is the summary:\" or any other extra text: Python is useful."
        )
        assert result == "FAKE SUMMARY"

def test_translate():
    with patch("ai_toolkit.call_gemini") as mock:
        mock.return_value = "FAKE TRANSLATION"
        result = translate("Hello, how are you?", "Spanish")
        mock.assert_called_once_with(
            "Translate the following text to Spanish. Return only the translated text, without explanations or extra text: Hello, how are you?"
        )
        assert result == "FAKE TRANSLATION"

def test_sentiment():
    with patch("ai_toolkit.call_gemini") as mock:
        mock.return_value = "Positive"
        result = sentiment("I love this product!")
        mock.assert_called_once_with(
            "I love this product! Analyze the sentiment of the text above:  Respond with exactly one word: Positive, Negative, or Neutral."
        )
        assert result == "Positive"


