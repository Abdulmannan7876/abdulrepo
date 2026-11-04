import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
engine.say(text)
engine.runAndWait()

def take_command():
with sr.Microphone() as source:
print("Listening...")
recognizer.adjust_for_ambient_noise(source, duration=1)
print("Speak now...")

```
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        query = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", query)
        return query.lower()

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""
```

def respond(command):
if "how are you" in command:
speak("Abdul, I am fine. How can I help you?")

```
elif "your name" in command:
    speak("I am Jarvis, your personal assistant.")

elif "hello" in command or "hi" in command:
    speak("Hello Abdul! How can I help you?")

elif "goodbye" in command or "exit" in command:
    speak("Goodbye Abdul!")
    return False

elif command:
    speak("Sorry Abdul, I don't know that yet.")

return True
```

if **name** == "**main**":
speak("Hey Abdul, I am listening.")

```
running = True

while running:
    command = take_command()

    if command:
        running = respond(command)
```
