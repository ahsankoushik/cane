<<<<<<< HEAD
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
=======
import os 


def speak(string:str):
    os.system(f'''espeak -s 150 "{string}" 2>/dev/null''')


if __name__ == '__main__':
    speak('hey this is john doe')
>>>>>>> origin/k_main
