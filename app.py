# ------------------- AI Chat Bot (Rule Based) -------------------------------

import datetime
import time

# ----------------------------- Data Provided to Bot ---------------------------
responses = {
    "hello": f"Hi there! How can I help you today?",
    "who are you": "I’m your friendly AI Chat Bot, at your service!.", 
    "how are you": "I’m just code, but I feel great when you run me!",
    "motivate me": "Keep going! Every bug you fix makes you a better coder 💪",
    "python": "Python is powerful — it can do AI, automation, and much more!",
    "sad": "Don’t worry! Even code breaks sometimes, but it always runs again 😊",
    "happy": "That’s great to hear! Keep that positive energy going 🎉",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}", 
    "bye": "Goodbye! Keep learning and keep smiling 😀",
    "date": f"Today's date is {datetime.date.today()}",
    "what is your name": "I am a Bot, so I don't have a name, but you can call me anything you want 😄",
    "tell me a thought": "Honesty is The Best Policy!"
}
keys = responses.keys()

# ----------------------- Chat Bot Functions ------------------------------------
def ChatBotResponse(prompt):
    search = prompt.lower()
    keys = responses.keys()
    for key in keys:
        if search == key:
            reply = responses[key]
            return reply
    return "Hmmm...., I don't have any idea about this. I'll tell you when I know."

def Greeting():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"

# ------------------------- Chat Bot Processing -----------------------------------
print("-------------------------------------- AI Chat Bot (Rule-Based)--------------------------------------\n")
name = input("🤖 Bot: Please Enter your name: ")
print("Thinking...\n")
time.sleep(3)
loop = True
print(f"🤖 Bot: Hi {name}!, {Greeting()}, How can I help you today ?: ")
while loop == True:
    prompt = input("👦 User: ")
    time.sleep(1)
    reply = ChatBotResponse(prompt)
    print(f"🤖 Bot: {reply}\n")

# ------------------------------ Loop Processing ----------------------------------
    if "bye" in prompt.lower():
        print("---------------------------------------------------------------------------------------------------------------")
        break