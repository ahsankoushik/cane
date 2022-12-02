
from music import player
from location import location
# from voice_command import voice
from image_read import take_photo
from image_read import image_read
import time
import os



#flags
menu = -1
next = False

while True:
    # print('m for music')

    if next:menu +=1
    
    else:
        inp = input('enter a menu: ')
        if inp == 'm' : 
            menu = (menu+1)%4


    if menu  == 0:
        player.play_for_once(os.getcwd()+'/voice_command/commads/music_mode.mp3')
        # time.sleep(2)
        player.kill_all = False
        a = player.MusicControl()
        time.sleep(1)
        b = player.MusicEnd()
        
        while 1:
            if player.kill_all:
                next = 1
                break 
            pass
        del a
        del b

    
    elif menu == 1:
        print(menu,'walking')
        player.play_for_once(os.getcwd()+'/voice_command/commads/walking_mode.mp3')
        # engine.save_to_file(location.address,'location.mp3')
        os.system(f'espeak -s 130 -g 11   "{location.address}" 2>/dev/null')
        # player.play_for_once('location.mp3')
        

        # location = '18 ulon road rampura dhaka'
        # voice.speak('now you are at '+location)
        # time.sleep(5)
        # time.sleep(5)
        if next: next = False
    
    elif menu == 2:
        print(menu,'image read')
        player.play_for_once(os.getcwd()+'/voice_command/commads/image_read.mp3')
        

        # voice.speak('image read mode')
        # time.sleep(2)
        if next: next = False

    elif menu == 3: 
        print(menu, 'detection')
        # player.play_for_once('/voice_command/commands/image_detection.mp3')
        player.play_for_once(os.getcwd()+'/voice_command/commads/image_detection.mp3')
        take_photo.capture_write('first.jpg')
        image_text = image_read('first.jpg')
        os.system(f'espeak -s 130 -g 11   "{image_text}" 2>/dev/null')


        

        # time.sleep(2)
        if next: next = False
    

