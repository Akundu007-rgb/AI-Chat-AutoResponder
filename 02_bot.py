import pyautogui
import time
import pyperclip
from openai import OpenAI
import os
import re   # ⚡ For text cleaning (timestamps & sender names)
import keyboard  # ⚡ For Esc key stop

# --- Configuration ---
# ✅ Make sure you have set your API key in your environment variables.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ⚡ Enable PyAutoGUI failsafe (move mouse to top-left corner to stop)
pyautogui.FAILSAFE = True

# --- Function to check if last message is from a specific sender ---
def is_last_message_from_sender(chat_log, senders_name="Didi"):
    try:
        # Match timestamps like /2025], /2026], etc.
        parts = re.split(r"/\d{4}\]", chat_log.strip())
        if not parts:
            return False
        last_message = parts[-1]
        return senders_name.lower() in last_message.lower()
    except Exception as e:
        print(f"[DEBUG] Error in is_last_message_from_sender: {e}")
        return False

# Small delay to let you switch to the correct window before execution
print("Starting in 3 seconds... Move to the right screen/window.")
time.sleep(3)

# Step 1: Click on the icon at (1404, 1055)
pyautogui.click(1263, 1060)
time.sleep(1)  # Wait for the app to open or focus

while True:
    # ⚡ Stop the loop if Esc is pressed
    if keyboard.is_pressed('esc'):
        print("Esc pressed. Stopping script.")
        break

    # Step 2: Drag from (550, 140) to (1867, 945) to select text
    pyautogui.moveTo(724, 308)
    pyautogui.dragTo(1850, 930, duration=1.5, button='left')
    time.sleep(0.5)

    # Step 3: Copy selected text (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.click(1200, 915)

    # Step 4: Retrieve text from clipboard into a variable
    chat_history = pyperclip.paste()

    print(chat_history)

    # Step 5: Check if last message is from the sender
    if is_last_message_from_sender(chat_history):
        # --- API Call ---
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a person named Anirban Kundu who can speak hindi,english as well as bengali. You are a coder and from india. You analyze chat history and talk like Anirban Kundu. Output should be the next chat response (text message only no timestamps & names)"},
                    {"role": "user", "content": chat_history}
                ]
            )

            # --- Output ---
            response = completion.choices[0].message.content
            pyperclip.copy(response)

        except Exception as e:
            print(f"An error occurred during the API call: {e}")
            print("\n💡 Action Required: Please check your OpenAI billing page.")
            print("The API key likely has insufficient credit or has reached a spending limit.")

        # Step 6: Click where to paste
        pyautogui.click(860, 970)
        time.sleep(0.5)

        # Step 7: Paste and press Enter
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)
        pyautogui.press('enter')
