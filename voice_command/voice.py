import os 


def speak(string:str):
    os.system(f'''espeak -s 150 "{string}" 2>/dev/null''')


if __name__ == '__main__':
    speak('hey this is john doe')