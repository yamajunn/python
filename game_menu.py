import readchar
import time
import os
from timeout_decorator import timeout, TimeoutError
os.system('clear')
menu_count = 0
while True:
    menu_count += 1
    print('+',end='')
    print('-'*100,end='')
    print('+')
    for i in range(15):
        if i == 5:
            print('|                __________________________________________________________________                  |')
            print('|               ___________      _______        __            __     __    _________                 |')
            print('|              /          /    /  _____|      /  _ \         /  \   /  \   \    ____\\                |')
            print('|             /__     ___/    |  /  ____     /  /_\ \       /    \_/    \   \   \___                 |')
            print('|               /   /         |  | |__  |   /   __   \     /  /\    /\   \   \    ___\\               |')
            print('|              /   /     __    \  \__/  |  /   /  \   \   /  /  \__/  \   \   \   \_____             |')
            print('|             /__ /     /_/     \______ / /___/    \ __\ /__/          \___\   \_________\\           |')
            print('|          ________________________________________________________________________________          |')
        if i == 13 and menu_count % 2 == 0:
            print('|                                            _             _                                         |')
            print('|                                           | |           | |                                        |')
            print('|                                        ___| |_ __ _ _ __| |_                                       |')
            print("|                                       / __| __/ _` | '__| __|                                      |")
            print('|                                       \__ \ || (_| | |  | |_                                       |')
            print('|                                       |___/\__\__,_|_|   \__|                                      |')
            print('|                                                                                                    |')
        if i == 13 and menu_count % 2 == 1:
            print('|                                    ++==    _             _  ==++                                   |')
            print('|                                    ||     | |           | |   ||                                   |')
            print('|                                        ___| |_ __ _ _ __| |_                                       |')
            print("|                                       / __| __/ _` | '__| __|                                      |")
            print('|                                       \__ \ || (_| | |  | |_                                       |')
            print('|                                    || |___/\__\__,_|_|   \__| ||                                   |')
            print('|                                    ++==                     ==++                                   |')
        print('|',end='')
        print(' '*100,end='')
        print('|')
    print('+',end='')
    print('-'*100,end='')
    print('+')

    TIMEOUT_SEC = 1

    @timeout(TIMEOUT_SEC)
    def input_with_timeout():
        return readchar.readchar()

    if __name__ == '__main__':
        try:
            input_str = input_with_timeout()
            if input_str == ' ':
                break
        except TimeoutError:
            pass
    os.system('clear')
os.system('clear')
game_list = ['ジャンケン','ブラックジャック','バカラット','ポーカー','オセロ']
game_list_count = 0
game_count = 0
game_yazirushi_count = 0
while True:
    print('+',end='')
    print('-'*100,end='')
    print('+')
    for i in range(18):
        if i == 5:
            print('|                                _       _           _     _  _     _                                |')
            print('|                               | |     | | _______ | |   | || |   | |                               |')
            print('|                               | |_   _| ||  _____|| |_  | || |   | |                               |')
            print('|                               |   |_|   || |_____ |   |_| || |   | |                               |')
            print('|                               |  _   _  ||  _____||  _    || |   | |                               |')
            print('|                               | | |_| | || |_____ | | |_  || |___| |                               |')
            print('|                               |_|     |_||_______||_|   |_||_______|                               |')
        if game_list_count == 0 and game_count % 2 == 0 and i == 10:
            print('|                 //      /__７  / ７##    　/￣/  / ７ /￣/＿_____  /￣/  / ７   \\\\                 |')
            print('|                //---   /__７　/  /   _   　￣　 /　/ /　____   _/  ￣　 /　/  ---\\\\                |')
            print('|                \\\\---    ＿__ノ　/ /_  __7 ＿__ノ　/ /__ノ__/　/   ＿__ノ　/   ---//                |')
            print('|                 \\\\   /＿_____／   /_/   /＿____／   　 /＿_ノ   /＿____／       //                 |')
        if game_list_count == 0 and game_count % 2 ==1 and i == 10:
            print('|                         /__７  / ７##    　/￣/  / ７ /￣/＿_____  /￣/  / ７                      |')
            print('|                        /__７　/  /   _   　￣　 /　/ /　____   _/  ￣　 /　/                       |')
            print('|                         ＿__ノ　/ /_  __7 ＿__ノ　/ /__ノ__/　/   ＿__ノ　/                        |')
            print('|                      /＿_____／   /_/   /＿____／   　 /＿_ノ   /＿____／                          |')
        if game_list_count == 1 and game_count % 2 == 0 and i == 10:
            print('|          /￣￣￣￣/##　/二二二/         /￣￣￣￣/   /__７  /￣７##            /￣￣￣￣/          |')
            print('|       　　￣￣/　/ /￣＿＿_￣￣/_ _　  /  /￣/　/ 　/__７　/　/    _    _ _　 /  /￣/　/           |')
            print('|       　＿__ノ　/   　 __ノ　/ ＵＵ/7  ー  _/　/　   ＿__ノ　/　/_  __7 ＵＵ/7 ー _/　/            |')
            print('|        /＿___,／    /____,／     くノ　  /___ノ　　/＿___,.／　  /_/     くノ   /___ノ             |')
        if game_list_count == 1 and game_count % 2 == 1 and i == 10:
            print('|   //     /￣￣￣￣/##　/二二二/         /￣￣￣￣/   /__７  /￣７##            /￣￣￣￣/    \\\\    |')
            print('|  //---  　￣￣/　/ /￣＿＿_￣￣/_ _　  /  /￣/　/ 　/__７　/　/    _    _ _　 /  /￣/　/   ---\\\\   |')
            print('|  \\\\---  ＿__ノ　/   　 __ノ　/ ＵＵ/7  ー  _/　/　   ＿__ノ　/　/_  __7 ＵＵ/7 ー _/　/    ---//   |')
            print('|   \\\\   /＿___,／    /____,／     くノ　  /___ノ　　/＿___,.／　  /_/     くノ   /___ノ       //    |')
        if game_list_count == 0 and i == 15:
            print('|                                           [ ジャンケン : ブラックジャック : ...]                   |')
        if game_list_count == 1 and i == 15:
            print('|                           [ ジャンケン : ブラックジャック : バカラット : ...]                      |')
        print('|',end='')
        print(' '*100,end='')
        print('|')
    print('+',end='')
    print('-'*100,end='')
    print('+')
    game_count += 1
    TIMEOUT_SEC = 1

    @timeout(TIMEOUT_SEC)
    def input_with_timeout():
        return readchar.readchar()

    if __name__ == '__main__':
        try:
            input_str = input_with_timeout()
            if input_str == 'a':
                if game_list_count > 0:
                    game_list_count -= 1
            if input_str == 'd':
                game_list_count += 1
            if input_str == ' ':
                break
        except TimeoutError:
            pass
    os.system('clear')
if game_list_count == 0:
    import janken
    # janken.janken()
    pass