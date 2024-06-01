import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyaudio

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
            listener.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                return command
            else:
                talk("I'm listening for the keyword 'Alexa'. Please try again.")
    except sr.UnknownValueError:
        print("Could not understand audio")
        talk("Sorry, I did not catch that. Could you please repeat?")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        talk("Sorry, there was an issue with the request. Please try again later.")
    return ""

def run_alexa():
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif command:
            talk('Please say the command again.')
            

run_alexa()