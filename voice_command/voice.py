import pyttsx3


engine = pyttsx3.init()

# voices = engine.getProperty('voices')

engine.setProperty('voice','bengali')
engine.setProperty('rate',150)


def speak(s:str):
    engine.say(s)
    engine.runAndWait()

def save(s,path):
    engine.save_to_file(s,path)
    engine.runAndWait()
    



