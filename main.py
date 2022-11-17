import pyttsx3
import datetime
import speech_recognition as sr
import joblib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning !')

    elif hour >= 12 and hour < 16:
        speak('Good Afteenoon !')

    else:
        speak('Good Evening !')

    speak("How can I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        speak("Say that again please...")  # Say that again will be printed in case of improper voice
        return "Say that again please..."  # None string will be returned
    return query


def checkCovid(condition):
    if condition == 1:
        speak('You Have covid-19.')
    else:
        speak("You don't have covid-19.")


if __name__ == '_main_':
    wishme()
    array = []
    gender = 0
    age = ""
    fever = 0
    tired = 0
    cough = 0
    breath = 0
    sore = 0
    pains = 0
    nose = 0
    running_nose = 0
    diarrhea = 0

    filename = 'finalized_model.sav'
    loaded_model = joblib.load(filename)

    # while True:

    speak('Do you want know whether you have covid-19 or not?')
    query1 = takeCommand().lower()
    query1boolean = True
    #     while query1boolean:
    if 'yes' in query1:
        speak('okay')
        speak('can i know your gender?')
        query2boolean = True
        while query2boolean:
            query2 = takeCommand().lower()
            if 'mail' in query2:
                gender = 1
                query2boolean = False
            elif 'female' in query2:
                gender = 0
                query2boolean = False
            else:
                query2boolean = True

        speak('Let me know your age?')
        query3 = takeCommand().lower()

        age = query3

        speak('Do you feel any sort of feverishness?')
        query4boolean = True
        while query4boolean:
            query4 = takeCommand().lower()
            if 'yes' in query4:
                fever = 1
                query4boolean = False
            elif 'no' in query4:
                fever = 0
                query4boolean = False
            else:
                query2boolean = True

        speak('Any kind of tiredness?')
        query5 = takeCommand().lower()
        if 'yes' in query5:
            tired = 1
        else:
            tired = 0

        speak('Do you have dry cough?')
        query6 = takeCommand().lower()
        if 'yes' in query6:
            cough = 1
        else:
            cough = 0

        speak('Do you feel difficulty in breathing?')
        query7 = takeCommand().lower()
        if 'yes' in query7:
            breath = 1
        else:
            breath = 0

        speak('Is your throat sore?')
        query8 = takeCommand().lower()
        if 'yes' in query8:
            sore = 1
        else:
            sore = 0

        speak('Do you have body pains?')
        query9 = takeCommand().lower()
        if 'yes' in query9:
            pains = 1
        else:
            pains = 0

        speak('Is your nose clogged?')
        query10 = takeCommand().lower()
        if 'yes' in query10:
            nose = 1
        else:
            nose = 0

        speak('are you suffering with running nose?')
        query11 = takeCommand().lower()
        if 'yes' in query11:
            running_nose = 1
        else:
            running_nose = 0

        speak('Do you have any symptoms of Diarrhea?')
        query12 = takeCommand().lower()
        if 'yes' in query12:
            diarrhea = 1
        else:
            diarrhea = 0
        query1boolean = False
        query2boolean = False
        query4boolean = False
    else:
        speak('no')
        query1boolean = False

    # output = loaded_model.predict([[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1]])[0]
    # checkCovid(output)
    age1 = 0
    age2 = 0
    age3 = 0
    age4 = 0
    age5 = 0
    gender1 = 0
    gender2 = 0

    if 0 < int(age) <= 9:
        age1 = 1
    elif 10 <= int(age) <= 19:
        age2 = 1
    elif 20 <= int(age) <= 24:
        age3 = 1
    elif 25 <= int(age) <= 59:
        age4 = 1
    elif int(age) >= 60:
        age5 = 1

    if gender == 1:
        gender1 = 1
    else:
        gender2 = 1

    output = loaded_model.predict([[fever, tired, cough, breath, sore, 0, pains, nose, running_nose, diarrhea, 0, age1,
                                    age2, age3, age4, age5, gender1, gender2, 0, 0, 1]])[0]
    checkCovid(output)

    # output = [[fever],[tired]

    # checkCovid(0)
    #     # speak(results)

# gender = 0
# age = ""
# fever = 0
# tired = 0
# cough = 0
# breath = 0
# sore = 0
# pains = 0
# nose = 0
# running_nose = 0
# diarrhea = 0