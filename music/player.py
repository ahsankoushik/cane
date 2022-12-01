from threading import Thread
import time 
# import datetime
from mutagen.mp3 import MP3
from pygame import mixer
# import threading
import os 


#flag 
paused = 1
volume = 0.7
kill_all = 0
play_time =0 
sleep_timer = 0

music_dir = f'{os.getcwd()}/musics/'
music_list =sorted([x for x in os.listdir(music_dir) if x.split('.')[1]=='mp3'])
print(music_list)
music_count = 0
total_music = len(music_list)




# Starting the mixer

# Start playing the song

def play_for_once(path):
    mixer.init(22050)

    # Setting the volume
    mixer.music.set_volume(volume)
    mixer.music.load(path)
    mixer.music.play()
    time.sleep(MP3(path).info.length)
    # time.sleep(3)
    mixer.music.unload()
    mixer.stop()
    mixer.quit()
    print('once fucntion done')


def play_maintain(mixer,count:int,step:int,total_music:int,music_list:list,music_dir:str):
    count = (count+step) % total_music
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load(music_dir+music_list[count])
    mixer.music.play()

    global sleep_timer
    global music_count
    global play_time 

    sleep_timer = MP3(music_dir+music_list[count]).info.length
    music_count = count
    play_time = 0 
    return count






class MusicControl(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        # self._stop_event = threading.Event()
        self.start()

    def run(self):
        print('thread started')
        mixer.init(22050)

        # Setting the volume
        
        global sleep_timer
        global paused 
        global volume
        global music_count
        # Loading the song
        mixer.music.set_volume(volume)
        mixer.music.load(music_dir + music_list[music_count])
        sleep_timer = MP3(music_dir+music_list[music_count]).info.length
        
        mixer.music.play()
        paused = 0 


        while True:	
            print('''m -> change menu 
p -> play or pause
> -> next song
< -> prevous song
+ -> volume up
- -> volume down''')

            query = input(" ")
            if query == 'p':
                # Pausing the music
                if not  paused:
                    mixer.music.pause()	
                    paused = 1
                # Resuming the music
                else:
                    mixer.music.unpause()
                    paused = 0 

            elif query == 'm':
                # Stop the mixer
                mixer.music.stop()
                mixer.quit()
                global kill_all 
                kill_all = 1
                # mixer.quit()
                break
            
            elif query == '>':
                
                play_maintain(mixer,music_count,1,total_music,music_list,music_dir)

            elif query == "<":

                play_maintain(mixer,music_count,-1,total_music,music_list,music_dir)

            elif query == '+' :
                volume += .1
                mixer.music.set_volume(volume)
            elif query == '-' :
                volume -= 0.1
                mixer.music.set_volume(volume)
            
            




class MusicEnd(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        # self._stop_event = threading.Event()
        self.start()
    def run(self):
        global sleep_timer
        global paused
        global play_time
        global kill_all
        # print(x,sleep_timer)
        while True:
            
            if not paused: play_time +=1
            # else: print('paused')
            if play_time > sleep_timer-1: 
                # print(x,sleep_timer)
                # print('next')
                global music_count
                music_count = play_maintain(mixer,music_count,1,total_music,music_list,music_dir)
                play_time = 0
                time.sleep(2)
            time.sleep(1)
            if kill_all:
                break






if __name__ == '__main__':

    MusicControl()
    time.sleep(.5)
    MusicEnd()
    while True:
        if kill_all:
            break 
        pass
