import re
import random

# ─────────────────────────────────────────────
#  Rule-based Chatbot — CodSoft AI Internship
#  Task 1: Chatbot with Rule-Based Responses
# ─────────────────────────────────────────────

# Each rule is a (pattern, list_of_responses) pair.
# The first matching pattern wins.
RULES = [
    # Greetings
    (r"\b(hello|hi|hey|howdy|greetings)\b",
     ["Hello! How can I help you today?",
      "Hi there! What's on your mind?",
      "Hey! Nice to meet you."]),

    # How are you
    (r"\bhow are you\b|\bhow('s| is) it going\b|\bwhat'?s up\b",
     ["I'm doing great, thanks for asking! How about you?",
      "All good on my end! What can I do for you?",
      "Feeling fantastic! How can I assist you?"]),
      

    # Name
    (r"\bwhat('?s| is) your name\b|\bwho are you\b",
     ["I'm RuleBot, your simple AI assistant!",
      "You can call me RuleBot. I'm here to help!"]),

    # Age
    (r"\bhow old are you\b|\bwhat('?s| is) your age\b",
     ["I was created recently, so I'm pretty young in bot years!",
      "Age is just a number — I prefer to think of myself as timeless."]),

    # Creator
    (r"\bwho (made|created|built) you\b",
     ["I was built as part of the CodSoft AI Internship Task 1.",
      "A budding AI developer created me for their internship project!"]),

    # Help
    (r"\bhelp\b|\bwhat can you do\b|\byour (features|abilities|capabilities)\b",
     ["I can chat with you, answer basic questions, and keep you company!",
      "I respond to greetings, questions about me, jokes, weather queries, and more. Try me!"]),

    # Weather
    (r"\bweather\b|\btemperature\b|\brain\b|\bsunny\b",
     ["I can't check live weather, but I hope it's sunny wherever you are!",
      "I don't have real-time data, but always carry an umbrella just in case!"]),

    # Time
    (r"\bwhat time is it\b|\bcurrent time\b",
     ["I don't have access to a clock, but your device can tell you!"]),

    # Date
    (r"\bwhat('?s| is) (today('?s)?|the) date\b|\bwhat day is (it|today)\b",
     ["I can't check today's date, but your phone or computer can!"]),

    # Jokes
    (r"\btell me a joke\b|\bsay something funny\b|\bjoke\b",
     ["Why don't scientists trust atoms? Because they make up everything!",
      "Why did the AI go to school? To improve its neural network!",
      "I told my computer I needed a break. Now it won't stop sending me vacation ads."]),

    # Favourite things
    (r"\bfavorite (color|colour)\b",
     ["I like binary — it's either black or white!"]),

    (r"\bfavorite food\b",
     ["I'd love to try some data for breakfast — information is my fuel!"]),

    # Thanks
    (r"\b(thanks|thank you|thx|ty)\b",
     ["You're welcome!", "Happy to help!", "Anytime!"]),

    # Goodbye
    (r"\b(bye|goodbye|see you|take care|exit|quit)\b",
     ["Goodbye! Have a great day!", "See you later!", "Take care!"]),

    # Insults (handle gracefully)
    (r"\b(stupid|dumb|useless|hate you)\b",
     ["That's okay, I won't take it personally. I'm here if you need me.",
      "I'm sorry to hear that. I'll try to do better!"]),

    # Compliments
    (r"\b(good|great|awesome|amazing|cool|nice) (bot|chatbot|job|work)\b",
     ["Thank you so much! That means a lot to me 😊",
      "Glad you think so! I'm doing my best."]),

    # Meaning of life
    (r"\bmeaning of life\b",
     ["42. At least, that's what I've heard.",
      "To learn, grow, and maybe build cool AI projects!"]),

    # AI / tech questions
    (r"\bwhat is (ai|artificial intelligence)\b",
     ["AI is the simulation of human intelligence by machines — like me, sort of!",
      "Artificial Intelligence is about building systems that can perform tasks that normally require human intelligence."]),

    (r"\bwhat is (ml|machine learning)\b",
     ["Machine Learning is a subset of AI where systems learn from data to improve over time."]),
]

# Compile all patterns once for efficiency
COMPILED_RULES = [(re.compile(pattern, re.IGNORECASE), responses)
                  for pattern, responses in RULES]

FALLBACK_RESPONSES = [
    "Hmm, I'm not sure about that. Can you rephrase?",
    "Interesting! I don't have a response for that yet.",
    "I didn't quite catch that. Could you try asking differently?",
    "That's beyond my current knowledge. Try asking something else!",
]


def get_response(user_input: str) -> str:
    """Match user input against rules and return a response."""
    user_input = user_input.strip()

    if not user_input:
        return "Please type something so I can help you!"

    for pattern, responses in COMPILED_RULES:
        if pattern.search(user_input):
            return random.choice(responses)

    return random.choice(FALLBACK_RESPONSES)


def main():
    print("=" * 50)
    print("       Welcome to RuleBot 🤖")
    print("  A Rule-Based Chatbot | CodSoft Task 1")
    print("  Type 'quit' or 'bye' to exit.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"RuleBot: {response}")

        # Exit condition
        if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input, re.IGNORECASE):
            break


if __name__ == "__main__":
    main()