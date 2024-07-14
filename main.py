import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib


# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')

# Get the details of the current voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice to the second option (female voice)

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()  # Wait for the speech to finish

def wishMe():
    """Wishes the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you, sir?")

def takeCommand():
    """Listens for user input from the microphone and returns it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Could you please say that again?")
        return "none"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "none"
    return query
def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
       query =takeCommand().lower()

       #logic for executng tasks based on query
       if 'wikipedia' in query:
           speak("searching wikipedia..")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("according to wikipedia")
           print(results)
           speak(results)

       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("googel.com")
       elif 'the time' in query:
           strTime=datetime.datetime.now().strftime("%h:%M:%")
       elif 'email to harry' in query:
        try:
           speak("What should I say?")
           content = takeCommand()
           to = "lalithkumar.m01@gmail.com"
           sendEmail(to, content)
           speak("Email has been sent!")
        except Exception as e:
           print(e)
           speak("Sorry my friend. I am not able to send this email")
       elif 'quit' in query:
           speak('thank you sir ,hope i am usefull')
           exit()
