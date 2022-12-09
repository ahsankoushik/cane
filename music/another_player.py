from pygame import mixer
# from pygame import AUDIO_ALLOW_FREQUENCY_CHANGE
import os
import time
import pygame
from threading import Thread


kill_all = 0

music_dir = f'{os.getcwd()}/musics/'
music_list = sorted([x for x in os.listdir(music_dir) if x.split('.')[1]=='mp3'])
print(music_list)
music_count = 0
total_music = len(music_list)
# print(music_dir+music_list[music_count])

# mixer.init(44100,16,2,2048)
mixer.init(22050 )
mixer.music.load(music_dir+music_list[0])

def play_once(path):
    global mixer
    mixer.music.unload()
    mixer.music.load(path)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.music.unload()
    mixer.music.load(music_dir+music_list[music_count])

    


def prev_next(mixer,step):
    global music_count
    global music_dir
    global music_list
    global total_music
    music_count = (music_count+step) % total_music
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load(music_dir+music_list[music_count])
    maintain()


def maintain():
    global mixer
    mixer.music.play()
    while mixer.music.get_busy():
        if kill_all: break
        time.sleep(1)
    else:
        prev_next(mixer,1)


def inp():
    global kill_all
    while 1:
        i = input()
        if i.strip() == 'm': 
            mixer.stop()
            kill_all = 1
            break
        elif i.strip() == '>':
            prev_next(mixer,1)
        elif i.strip() == '<':
            prev_next(mixer,-1)
        




th1 = Thread(target=maintain)
th2 = Thread(target=inp)



if __name__ == '__main__':


    th1.start()
    th2.start()




                



