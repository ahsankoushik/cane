import pyttsx3
import os

engine = pyttsx3.init()

# voices = engine.getProperty('voices')

# for x in voices:
#     print(x)

# engine.setProperty('voice','bengali')
# engine.setProperty('bit',)


def speak(s:str):
    engine.say(s)
    engine.runAndWait()

def save(s,path):
    engine.save_to_file(s,path)
    engine.runAndWait()
    

# speak('hey this is kanak')

if __name__ == '__main__':
    speak('hello world')
    save('this is koushik','test.mp3')