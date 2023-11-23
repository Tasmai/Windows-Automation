import pyttsx3 #tts
import datetime
import speech_recognition as sr
#import pyaudio
import webbrowser
import os
import pyautogui
import sys
#pip install auto-py-to-exe

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
        
    speak("I am Blue Horse a i.... Tell me how may I help you.")

def get_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1

        audio = rec.listen(source)

        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None"

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query
    
if __name__ == '__main__':
    wish_user()
    print('Welcome to Blue horse A.I')
    while True: 
        query = get_command().lower()
        home_user_dir = os.path.expanduser("~")

        if 'who are you' in query:
            speak("I am Blue Horse personal assistant.... developed by tasz")

        elif 'minimise window' in query.lower() or "minimize window" in query.lower():
            speak('minimizing window')
            pyautogui.hotkey("winleft", "down")  # Minimize the current window

        elif 'maximize window' in query.lower() or "maximise window" in query.lower():
            speak('maximizing window')
            pyautogui.hotkey("winleft", "up")  # Maximize the current window

        elif 'close window' in query.lower():
            speak('Closing window')
            pyautogui.hotkey("alt", "f4")  # Close the current window



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.today().strftime('%Y-%m-%d')
            print(strDate)
            speak(f"The date is {strDate}")




        elif 'open calculator' in query.lower():
            speak('Opening calculator')
            os.system("calc")  # Open the calculator
        # elif 'close calculator' in query:
        #     fun_talk('Closing calculator')
        #     os.system("TASKKILL /F /IM calc")

        elif 'open notepad' in query:
            speak('Opening notepad')
            os.startfile("C:\\Windows\\notepad.exe")
        elif 'close notepad' in query:
            speak('Closing notepad')
            os.system("TASKKILL /F /IM notepad.exe")


        elif 'open spotify' in query.lower():
            speak('Opening Spotify')
            os.system("C:\\Users\\taszg\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe")
        elif 'close spotify' in query:
            speak('Closing Spotify')
            os.system("TASKKILL /F /IM Spotify.exe")

        

        elif 'open firefox' in query:
            speak('Opening firefox')
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        elif 'close firefox' in query:
            speak('closing firefox')
            os.system("TASKKILL /F /IM firefox.exe")

        elif 'open chrome' in query:
            speak('Opening chrome')
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'close chrome' in query:
            speak('closing chrome')
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("www.google.com")



        elif 'exit' in query:
            speak("Shutting down....until next time")
            sys.exit()

