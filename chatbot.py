# chatbot.py
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi! How can I help you today?"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that yet."
