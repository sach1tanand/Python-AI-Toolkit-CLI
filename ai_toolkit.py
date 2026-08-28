# Load the api key from the .env file
import argparse
import os

from dotenv import load_dotenv
from google import genai


MODEL = "gemini-3.6-flash"

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)

def call_gemini(instruction):
    interaction = client.interactions.create(
        model=MODEL,
        input=instruction
    )
    return interaction.output_text


def summarize(text):
    instruction = "Summarize the following text concisely. Return only the summary. Do not add phrases like \"Here is the summary:\" or any other extra text: " + text
    return call_gemini(instruction)

def translate(text,language):
    instruction=f"Translate the following text to {language}. Return only the translated text, without explanations or extra text: {text}"
    return call_gemini(instruction)

def sentiment(text):
    instruction=f"{text} Analyze the sentiment of the text above:  Respond with exactly one word: Positive, Negative, or Neutral."
    return call_gemini(instruction)

def main():

    parser=argparse.ArgumentParser(
        prog="ai_toolkit.py",
        description="A command line tool for text summarization, translation, and sentiment analysis using Google's Gemini model.",
    )



    subparsers=parser.add_subparsers(required=True)
    summarize_parser=subparsers.add_parser("summarize")
    translate_parser=subparsers.add_parser("translate")
    sentiment_parser=subparsers.add_parser("sentiment")



    summarize_parser.add_argument("text")
    translate_parser.add_argument("text")
    translate_parser.add_argument("--language", required=True)
    sentiment_parser.add_argument("text")

    summarize_parser.set_defaults(
        func=summarize,
        command="summarize"
    )

    translate_parser.set_defaults(
        func=translate,
        command="translate"
    )

    sentiment_parser.set_defaults(
        func=sentiment,
        command="sentiment"
    )

    args=parser.parse_args()

    
    if args.command == "translate":
        result = args.func(args.text, args.language)
    else:
        result = args.func(args.text)
    print(result)
   

if __name__ == "__main__":
    main()
