import pyttsx3

#runs tts by the use of inbuilt tts on a computer
engine = pyttsx3.init()

engine.say(get_response)
engine.runAndWait()