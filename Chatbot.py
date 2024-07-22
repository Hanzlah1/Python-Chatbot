import random

greetings = ["Hello", "Hi", "Hey"]
responses = ["How are you?", "What's up?", "How can I help you?"]

def chatbot(message):
	if message in greetings:
		return random.choice(responses)
	elif message == "bye":
		return "Goodbye!"
	else:
		return "I didn't understand that. Please try again."

print(chatbot("Hello"))  # Output: How are you?
print(chatbot("Hi"))  # Output: What's up?
print(chatbot("Hey"))  # Output: How can I help you?
