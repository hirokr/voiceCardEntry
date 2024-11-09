import pyttsx3
import speech_recognition as sr 
import pyjokes 
import datetime
import pywhatkit
import wikipedia
from sys import exit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(command)
            return command
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def dataEntry():
    pass

# def initMembers(name):
    

def run_alexa():
    command = take_command()
    print(command)
    if not command:
        return

    print(command)
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song} on YouTube')
        pywhatkit.playonyt(song) # Uncomment if pywhatkit is installed and used

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(f'Current time is {time}')

    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, sentences=1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk("Sorry, I have a headache")

    elif 'are you single' in command:
        talk('I am in a relationship with your Wi-Fi')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'exit' in command:
        talk('Closing the program')
        exit()

    elif 'hello' in command or 'hey' in command:
        talk('Hello, how may I help you?')

    else:
        talk('Please say the command again')

while True:
    run_alexa()
