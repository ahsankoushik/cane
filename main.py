
from music import player
import time

#flags
music = 0


while True:
    menu = input('enter a menu: ')

    if menu == 'm':
        if music == 0:
            a = player.MusicControl()
            b = player.MusicEnd()
            while 1:
                if player.kill_all:
                    break 
                pass
            del a
            del b


