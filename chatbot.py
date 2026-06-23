from ast import Name
from http.client import responses
import random
# Chatbot Name
BotName = "Chatbot"
# Questions and Answers
Responses = {
    "hello": [
        "Hey! How's it going?",
        "Hello! Good to see you.",
        "Hi! What can I do for you?"
    ],

    "hi": [
        "Hi! How can I help you today?",
        "Hey! What's up?"
    ],

    "how are you": [
        "I'm doing great!what about you?",
        "yeah, Running smoothly, no bugs today!(hopefully). How about you?",
        "I'm fine, thanks for asking! How are you?"
    ],

    "what is your name": [
        f"I'm {BotName}, your friendly chatbot.",
        f"They call me {BotName}."

    ],

    "who are you": [
        f"I'm {BotName} built  by Sharyar Ali ",
    ],

    "help": [
        "You can ask me how I'm doing, my name, for a joke, or just say hi. Type 'bye' to leave anytime.",
        "Try saying 'hello', 'joke', or 'what is your name' to get started."
    ],

    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I told my computer I needed a break, and it said 'no problem, I'll go to sleep.'",
        "There are 10 types of people: those who understand binary, and those who don't."
    ],

    "thank you": ["You're welcome!", "Anytime!"],
    "thanks": ["No problem at all!", "Glad I could help."],
    "what can you do": [
        "Right now I only know fixed rules like greetings, jokes, my own name, and a few small talk lines. No real thinking yet! But I'm learning more every day.",
    ],
}

# Words to end the conversation
ExitCommands = ["bye", "exit", "quit", "goodbye"]

ExitReplies = ["Goodbye! Take care.", "See you later!", "Shutting down... bye for now!"]

# Function to clean user input
def CleanText(RawText):
    """Lowercase, strip extra spaces, and drop basic punctuation so
    'Hello!' and 'hello' both match the same dictionary key."""
def CleanText(RawText):
    Text = RawText.lower().strip()

    for symbol in ["?", "!", ".", ","]:
        Text = Text.replace(symbol, "")
    return Text

# Function to find response based on user input
def GetResponse(UserText): 
    
       # Exact match
    if UserText in Responses:
        return random.choice(Responses[UserText])

    # If Partial match, check if any known phrase appears inside the
    # message (so "do you have a joke for me" still triggers "joke")
    for key in Responses:
        if key in UserText:
            return random.choice(Responses[key])

    # If nothing matches
    return "Sorry bruh, I didn't quite get that. Type 'help' if you need any else say goodBye."


def RunChatbot():
    print(f"{BotName}: Hey, I'm {BotName} your friendly chatbot,built  by Sharyar Ali.")
    print(f"{BotName}: Type 'bye', 'exit', or 'quit' whenever you want to stop.\n")

    while True:
        RawInputText = input("You: ")
        UserText = CleanText(RawInputText)

        #if the user input is empty, prompt them to say something
        if UserText == "":
            print(f"{BotName}: Go ahead, I'm listening!")
            continue

        #if the user input is an exit command, say goodbye and break the loop
        if UserText in ExitCommands:
            print(f"{BotName}: {random.choice(ExitReplies)}")
            break

        #if the user input is not empty or an exit command, get a response and print it
        reply = GetResponse(UserText)
        print(f"{BotName}: {reply}")

#start the chatbot if this file is run directly
if __name__ == "__main__":
    RunChatbot()
