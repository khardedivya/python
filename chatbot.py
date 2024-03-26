import random

# Define possible responses for the chatbot
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Feeling great, how about you?", "All good!"],
    "what's your name": ["I'm a chatbot.", "You can call me Chatbot!", "I don't have a name, I'm just a bot."],
    "bye": ["Goodbye!", "See you later!", "Bye bye!"]
}

# Function to get a response from the chatbot
def get_response(message):
    message = message.lower()
    for key in responses:
        if message in key:
            return random.choice(responses[key])
    return "I'm sorry, I didn't understand that."

# Main function to interact with the chatbot
def main():
    print("Welcome to the Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(get_response(user_input))
            break
        else:
            print("Chatbot:", get_response(user_input))

if __name__ == "__main__":
    main()
