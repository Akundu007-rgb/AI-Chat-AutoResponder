<h1 align="center">🤖 AI Chat AutoResponder</h1>

<p align="center">
  An intelligent desktop automation bot that reads chat messages and replies automatically using AI.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/OpenAI-GPT-green">
  <img src="https://img.shields.io/badge/Automation-PyAutoGUI-orange">
  <img src="https://img.shields.io/badge/Status-Experimental-yellow">
</p>

---

## 🚀 Overview

This project is a **desktop automation AI bot** that:

✅ Reads chat messages from screen  
✅ Detects sender  
✅ Generates intelligent replies using AI  
✅ Automatically pastes and sends the response  

It simulates a **human-like chat assistant** for real-time conversations.

---

## 🎯 Key Features

- 🖱️ Mouse automation using PyAutoGUI  
- 📋 Clipboard data extraction  
- 🧠 AI-generated responses (OpenAI API)  
- 🔍 Smart sender detection using regex  
- ⛔ Emergency stop using `Esc` key  
- ⚡ Real-time chat monitoring  

---

## 🛠️ Tech Stack

- 🐍 Python 3  
- 🖱️ pyautogui  
- 📋 pyperclip  
- ⌨️ keyboard  
- 🤖 OpenAI API  
- 🔍 regex (`re` module)

---

## ⚙️ How It Works

1. Selects chat area using mouse drag  
2. Copies chat text (Ctrl + C)  
3. Extracts messages from clipboard  
4. Detects last sender  
5. Sends chat history to AI  
6. Receives response  
7. Pastes & sends message automatically  

---

## 🧪 Demo Workflow


User sends message →
Bot detects new message →
AI generates reply →
Bot sends reply automatically


---

## 📂 Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/AI-Chat-AutoResponder.git
```
### 2️⃣ Install dependencies
```bash
pip install pyautogui pyperclip keyboard openai
```
### 3️⃣ Set API Key
Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```
```bash
Linux/Mac:
export OPENAI_API_KEY="your_api_key_here"
```
## ▶️ Usage
```bash
python main.py
```
👉 Switch to your chat window within **3 seconds**.

## ⚠️ Important Notes
- Coordinates are **screen-dependent** → adjust for your device
- Use carefully (automation may interfere with normal usage)
- Works best with web-based chat interfaces

## 🚧 Future Improvements
- 🎯 Auto-detect chat window (no fixed coordinates)
- 🖥️ GUI dashboard
- 🧠 Context memory (long conversations)
- 🔐 Better sender identification
- 📱 Multi-platform support

## 🧠 Learning Outcomes
- Desktop automation
- API integration
- Real-time system design
- Human-like AI interaction

## 🌟 Support
- If you like this project:
- ⭐ Star the repo
- 🍴 Fork it
- 📢 Share it

## ⚠️ Disclaimer
- This project is for educational purposes only.
- Use responsibly and avoid violating any platform policies.
