import pyttsx3

text = input("Enter the text: ")

# Print the text
print("Text:", text)

# Generate voice
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
