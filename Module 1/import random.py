import random

# Define predefined patterns and responses
patterns_responses = {
    "greeting": {
        "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
        "responses": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"]
    },
    "goodbye": {
        "patterns": ["Bye", "See you later", "Goodbye"],
        "responses": ["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."]
    },
    "thanks": {
        "patterns": ["Thanks", "Thank you", "That's helpful"],
        "responses": ["Happy to help!", "Any time!", "My pleasure"]
    },
    "hours": {
        "patterns": ["What hours are you open?", "What are your hours?", "When are you open?" ],
        "responses": ["We're open every day 9am-9pm", "Our hours are 9am-9pm every day"]
    },
    "mopeds": {
        "patterns": ["Which mopeds do you have?", "What kinds of mopeds are there?", "What do you rent?" ],
        "responses": ["We rent Yamaha, Piaggio, and Vespa mopeds", "We have Piaggio, Vespa, and Yamaha mopeds"]
    },
    "payments": {
        "patterns": ["Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?" ],
        "responses": ["We accept VISA, Mastercard, and AMEX", "We accept most major credit cards"]
    },
    "opentoday": {
        "patterns": ["Are you open today?", "When do you open today?", "What are your hours today?","duke"],
        "responses": ["We're open every day from 9am-9pm", "Our hours are 9am-9pm every day"]
    },
    "rental": {
        "patterns": ["Can we rent a moped?", "I'd like to rent a moped", "How does this work?" ],
        "responses": ["Are you looking to rent today or later this week?"],
        "context_set": "rentalday"
    },
    "today": {
        "patterns": ["today","duke" ],
        "responses": ["For rentals today please call 1-800-MYMOPED", "Same-day rentals please call 1-800-MYMOPED"],
        "context_filter": "rentalday"
    }
    # Add more intents and responses similarly
}

def get_response(intent):
    responses = patterns_responses[intent]["responses"]
    return random.choice(responses)

def chat():
    print("Start talking with the bot (type 'exit' to stop):")
    while True:
        user_input = input("You: ").capitalize().strip()
        if user_input == 'Exit':
            print("Bot: Goodbye!")
            break

        # Implement intent matching
        matched_intent = None
        for intent, data in patterns_responses.items():
            if user_input in data["patterns"]:
                matched_intent = intent
                break

        if matched_intent:
            bot_response = get_response(matched_intent)
            print(f"Bot: {bot_response}")
        else:
            print("Bot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chat()