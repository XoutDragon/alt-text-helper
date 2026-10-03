import pyttsx3

def tts(text: str):
    # Skip non-spoken syntax characters if present
    text = text.strip()
    if not text:
        return

    engine = pyttsx3.init()
        
    engine.say(text)
    engine.runAndWait()