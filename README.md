# AI Chat Assistant

A simple, safe, and user-friendly chat assistant powered by OpenAI's GPT-4 through OpenRouter API. The application includes time-based greetings, content moderation, and safety features.

## Features

- 🕒 Time-based greetings (morning/afternoon/evening)
- 🛡️ Built-in content moderation
- ⚠️ Keyword filtering for unsafe content
- 🔄 Continuous interaction loop
- 🚫 Input validation
- 🤖 Integration with OpenRouter API (using GPT-4)

## Prerequisites

- Python 3.x
- OpenRouter API key

## Installation

1. Clone the repository or download the source code.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your OpenRouter API key:

```
OPENROUTER_API_KEY=your_api_key_here
```

## Usage

Run the program using Python:

```bash
python main.py
```

The program will:

1. Display a time-appropriate greeting
2. Wait for your input
3. Process your request while checking for banned content
4. Return the AI's response (with moderation if necessary)

To exit the program, type "exit" or "quit".

## Safety Features

The application includes several safety measures:

- Pre-defined list of banned keywords
- Input moderation before API calls
- Output moderation of AI responses
- Automatic redaction of potentially harmful content

## Configuration

You can modify the following in `main.py`:

- `BANNED_KEYWORDS`: List of words to be filtered
- `system_prompt`: The base prompt that defines the AI's behavior
- Model selection in the API call

## Environment Variables

- `OPENROUTER_API_KEY`: Your OpenRouter API key (required)

## Error Handling

The application includes error handling for:

- Empty inputs
- API errors
- Banned content

## Note

Remember to update the `<YOUR_SITE_URL>` and `<YOUR_SITE_NAME>` placeholders in the code with your actual website information if you plan to track rankings on openrouter.ai.
