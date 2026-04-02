from openai import OpenAI
import os

# --- Configuration ---
# ✅ Make sure you have set your API key in your environment variables.
# For example, in PowerShell: $env:OPENAI_API_KEY="your_secret_key_here"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- API Call ---
command = """Shelley Hopkins
    Hi jay can you add dad to this chat as well? I tried to do it but I think it has to be Admin (you!)
    4:28 pm
    You removed Peter
    You added Dad
    Lol, here's a funny thing, I thought I'd added dad but turns out it was a completely random Peter
    4:30 pm
    Shelley Hopkins
    Hahahahah! I was thinking, who's number is this?!
    4:39 pm
    Yeah, Peter kept viewing the messages so when dad told me he wasn't sure if he'd been added I was like 'Dude, you're viewing the messages'
    4:40 pm
    Shelley Hopkins
    Hahahahahaha! Ooooops!"""
try:
    # NOTE: Using 'gpt-4o-mini' as it is the most cost-effective and
    # generally available model, allowing you to test the API for free/cheaply.
    completion = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are a person named Ani who can speak hindi,english as well as bengali. He is a coder and from india. You analyze chat history and talk like ani"},
            {"role": "user", "content": command}
        ]
    )

    # --- Output ---
    print("--- Jarvis's Response ---")
    print(completion.choices[0].message.content)

except Exception as e:
    # This block will catch the 'insufficient_quota' error, but uses a general error message
    print(f"An error occurred during the API call: {e}")
    print("\n💡 Action Required: Please check your OpenAI billing page.")
    print("The API key likely has insufficient credit or has reached a spending limit.")