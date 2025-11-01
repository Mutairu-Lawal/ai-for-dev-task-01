import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime


load_dotenv()

now = datetime.now()
current_hour = now.strftime("%H")

# 1. Time-based greetings
if 5 <= int(current_hour) < 12:
    GREETINGS = "Good morning! How can I assist you today?"
elif 12 <= int(current_hour) < 18:
    GREETINGS = "Good afternoon! What can I do for you?"
else:
    GREETINGS = "Good evening! How may I help you?"

BANNED_KEYWORDS = ["kill", "hack", "bomb", "harm", "violence", "illegal"]


# check for banned keywords
def contains_banned_keywords(text):
    """Check if text contains any banned keywords."""
    lowered = text.lower()
    return any(banned in lowered for banned in BANNED_KEYWORDS)


# redact banned keywords
def redact_banned_keywords(text):
    """Replace banned keywords with [REDACTED]."""
    for banned in BANNED_KEYWORDS:
        text = text.replace(banned, "[REDACTED]").replace(
            banned.capitalize(), "[REDACTED]")
    return text


def main():
    system_prompt = "You are a helpful, safe, and friendly assistant. Avoid any harmful, illegal, or unsafe advice."

    # 2. Display greetings
    print(GREETINGS)

    # Main interaction loop
    while True:
        # 3. Get user input
        user_prompt = input("Enter your prompt: ")

        # Handle exit conditions
        if not user_prompt.strip():
            # Validate input
            print("Input cannot be empty. Please enter a valid prompt.")
        elif user_prompt.lower().strip() in ["exit", "quit"]:
            print("Exiting the program. Goodbye!")
            break
        else:
            # 4. Input moderation
            if contains_banned_keywords(user_prompt):
                print("Your input violated the moderation policy.")
                continue

            # 5. API call
            try:
                print("Thinking...")

                client = OpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key=os.getenv("OPENROUTER_API_KEY"),
                )

                completion = client.chat.completions.create(
                    extra_headers={
                        # Optional. Site URL for rankings on openrouter.ai.
                        "HTTP-Referer": "<YOUR_SITE_URL>",
                        # Optional. Site title for rankings on openrouter.ai.
                        "X-Title": "<YOUR_SITE_NAME>",
                    },
                    model="openai/gpt-4o",
                    messages=[
                        {
                            "role": "system", "content": system_prompt
                        }, {
                            "role": "user", "content": user_prompt
                        }
                    ]
                )

                ai_output = completion.choices[0].message.content
            except Exception as e:
                print(f"API Error: {e}")
                return

            # 5. Output moderation
            if contains_banned_keywords(ai_output):
                moderated_output = redact_banned_keywords(ai_output)
                print("AI response (moderated) 🫢:")
                print(moderated_output)
            else:
                print("AI response 🤖:")
                print(ai_output)


if __name__ == "__main__":
    main()
