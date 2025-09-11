import speech_recognition as sr
import pyttsx3
import threading
import pywhatkit
import datetime
import wikipedia
import time

# Initialize recognizer
listener = sr.Recognizer()

# ---------- NEW TALK FUNCTION ----------
def talk(text):
    print(f"Assistant: {text}")

    def speak():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        
        engine.stop()

    threading.Thread(target=speak, daemon=True).start()
# --------------------------------------

def take_command():
    try:
        with sr.Microphone() as source:
       
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User: {command}")
    except:
        command = ""
    return command

def run_assistant():
    talk("Hello, I am your mini assistant. How can I help you?")
    while True:
        command= take_command()
        if 'play' in command:
            song = command.replace('play', '').strip()
            talk(f'Playing {song}') 
            pywhatkit.playonyt(song)

         # Tell time
        elif 'time' in command:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'The time is {time_now}')

        # Tell date
        elif 'date' in command:
            date_now = datetime.datetime.now().strftime('%A, %B %d, %Y')
            talk(f'Today is {date_now}')

        # Wikipedia search
        elif 'wikipedia' in command:
            person = command.replace('wikipedia', '')
            try:
                info = wikipedia.summary(person, sentences=2)
                talk(info)
                time.sleep(10)
            except:
                talk("Sorry, I couldn't find that on Wikipedia.")

        if 'exit' in command or 'stop' in command or 'bye' in command:
            talk("Goodbye! Have a great day.")
            break

run_assistant()        
