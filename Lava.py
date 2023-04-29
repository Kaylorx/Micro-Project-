import pyttsx3
import datetime
import SpeechRecognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')       # gets you the details of the current voice
engine.setProperty('voice', voice[1].id)    # 0-male voice , 1-female voice

def engine.say(audio)(audio):   
engine.say(audio)    
engine.runAndWait() #Without this command, speech will not be audible to us.
if __name__=="__main__" :    
engine.say(audio)('Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')


 def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine.say(audio)("Good Morning!")    
    
    elif hour>=12 and hour<18:
        engine.say(audio)("Good Afternoon!")       
    
    elif:
        engine.say(audio)("Good Evening!")      
   
    else:
     engine.say(audio)('Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')

def takeCommand():
    #It takes microphone input from the user and returns string output    
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.    
except Exception as e:
        # print(e)  use only if you want to print the error!
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() #Converting user query into lower case        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            engine.say(audio)('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            engine.say(audio)("According to Wikipedia")
            print(results)
            engine.say(audio)(results)

		elif 'open youtube' in query:
            webbrowser.open("youtube.com")

		elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            engine.say(audio)(f"Sir, the time is {strTime}")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

