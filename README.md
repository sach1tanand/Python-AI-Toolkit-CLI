# Python AI Toolkit CLI

A command-line AI toolkit that performs three text-processing tasks using an LLM API:

* **Summarization**
* **Translation**
* **Sentiment Analysis**

## Features

* CLI interface built with `argparse`
* Text summarization
* Text translation
* Sentiment analysis
* Environment-based API key management with `.env`
* Input validation for CLI arguments
* API error handling
* Automated tests using `pytest` and mocking
* Dependency management with `requirements.txt`

## Tech Stack

* **Python**
* **Gemini API**
* **argparse** — CLI argument parsing
* **python-dotenv** — environment variable management
* **pytest** — automated testing

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI_toolkit
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```
## Environment Setup

Create a `.env` file in the project root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

The API key is loaded from the environment using `python-dotenv`.

**Do not commit the `.env` file to GitHub.**

## Usage

### Summarize

```bash
python ai_toolkit.py summarize "I love Python"
```

### Translate

```bash
python ai_toolkit.py translate "I love Python" --language Spanish
```

### Sentiment Analysis

```bash
python ai_toolkit.py sentiment "I love Python"
```
## Testing

Run the automated tests with:

```bash
pytest test_ai_toolkit.py
```

The test suite uses `pytest` and mocking to test the AI functions without making real API calls.

## Project Structure

```text
AI_toolkit/
├── ai_toolkit.py          # Main CLI application
├── test_ai_toolkit.py     # Automated tests
├── requirements.txt       # Project dependencies
├── .env                   # API key (not committed)
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```
