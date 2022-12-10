import readchar
import os
import time
import random
os.system('clear')
def saisyoha():
    menu_count = 0
    select_hand = 0
    while True:
        print('+',end='')
        print('-'*100,end='')
        print('+')
        for i in range(21):
            if menu_count == 0 and i == 10:
                print('|                 ＿_l__　l　　ヽ 　 l　　　　　　  | 　‐┼‐　     _/‐-┐〃　　　　                    |')
                print('|                   ＿＼　|　　　）　|　　　　  ├　 |  __| 　      　 /　 　ー──　                   |')
                print('|                 （ ＿_　 V　　　　 ヽ__ノ 　ｄ-、 し(__jヽ     　_ノ　　　　　　  ロロロ           |')
                print('|                                                                                                    |')
                print('|                                                                                                    |')
                print('|                                                                                                    |')
                print('|                                                                                                    |')
                print('|                                                                                                    |')
                print('|                                                                                                    |')
            if menu_count >= 1 and i == 10:
                print('|                            ─　　〃　　　　 ＼　　　 ├‐┬‐　--　　.                                  |')
                print('|                            ─　 /　 -┼‐ｧ　　　　/　　　│ 　 　　/                                   |')
                print("|                            ＿／ 　  |'´ 　＿_／　　_ノ　 　__ノ　   ロロロ                         |")
            if menu_count >= 1 and select_hand == 0 and i ==20:
                print('|   ++==                 ==++                                                                        |')
                print("|   || 　/￣￣￣ /##       ||      　＿ノ￣/       　  ＿/￣/_　     　  / ７' ７ ロ                 |")
                print('|      /  /￣/　/ ________        /＿　　∠_         /__　　＿/     　   /　/i　l 　  ________        |')
                print("|     ー'　_/　/ |________|      /＿　　＿_/ 二二| /__　　＿_/        _ノ　/i　 i_  |________|       |")
                print('|　 ||  /___ノ　           ||    　/＿/      二二|   /＿/ 　　      /__,／　　ゝ､__|                 |')
                print('|   ++==                 ==++                                                                        |')
            if menu_count >= 1 and select_hand == 1 and i ==20:
                print('|                              ++==                         ==++                                     |')
                print("|      　/￣￣￣ /##           ||  　＿ノ￣/       　  ＿/￣/_||     　  / ７' ７ ロ                 |")
                print('|      /  /￣/　/ ________        /＿　　∠_         /__　　＿/     　   /　/i　l 　  ________        |')
                print("|     ー'　_/　/ |________|      /＿　　＿_/ 二二| /__　　＿_/        _ノ　/i　 i_  |________|       |")
                print('|　     /___ノ　               ||　/＿/      二二|   /＿/ 　　||    /__,／　　ゝ､__|                 |')
                print('|                              ++==                         ==++                                     |')
            if menu_count >= 1 and select_hand == 2 and i ==20:
                print('|                                                                 ++==                      ==++     |')
                print("|      　/￣￣￣ /##               　＿ノ￣/       　  ＿/￣/_　  ||　   / ７' ７ ロ          ||     |")
                print('|      /  /￣/　/ ________        /＿　　∠_         /__　　＿/     　   /　/i　l 　  ________        |')
                print("|     ー'　_/　/ |________|      /＿　　＿_/ 二二| /__　　＿_/        _ノ　/i　 i_  |________|       |")
                print('|　     /___ノ　                 　/＿/      二二|   /＿/ 　　    ||/__,／　　ゝ､__|          ||     |')
                print('|                                                                 ++==                      ==++     |')
            print('|',end='')
            print(' '*100,end='')
            print('|')
        print('+',end='')
        print('-'*100,end='')
        print('+')
        if menu_count == 0:
            time.sleep(1)
        if menu_count >= 1:
            read = readchar.readchar()
            if read == 'a':
                if select_hand > 0:
                    select_hand -= 1
            if read == 'd':
                if select_hand < 2:
                    select_hand += 1
            if read == ' ':
                return select_hand
                break
        menu_count += 1
        os.system('clear')
def janken():
    print('+',end='')
    print('-'*100,end='')
    print('+')
    for i in range(24):
        if i == 5:
            print('|                    　━　 ┃┃┃　　 　 ━　 ┃　┣━┳━ ━　 ┃  .━━┓　 　┏━┓　 　　┃　                      |')
            print('|                    　━　 ┃┃┃　　 　  　 ┃　┃ ┃ 　   ┃　   ┃　   ┣━┫　　 　┃　                      |')
            print('|                    　　  ┃　  　╋┓　 　 ┃ ┃  ┃　　 ┃　　 ┏┫ 　 ┃  ┃　━━━　┣━                       |')
            print('|                    　　 ┃ 　  　┃　 　 ┃　　 ┃ 　 ┃　   ┏┛┗┓　    ┃　 　　┃　                      |')
            print('|                    　━━┛ 　   　┃　　━━┛　  ┛　━━┛ 　  ┃　 ┗　　 ┛　    　┃　                      |')
        if i == 15:
            print('|                                          ---スペース---                                            |')
        print('|',end='')
        print(' '*100,end='')
        print('|')
    print('+',end='')
    print('-'*100,end='')
    print('+')
    readchar.readchar()
    os.system('clear')
    select_hand = saisyoha()
    os.system('clear')
    katimake_count = 0
    aiko = 0
    enemy_janken = random.randint(0,2)
    while True:
        print('+',end='')
        print('-'*100,end='')
        print('+')
        for i in range(18):
            if katimake_count == 0 and enemy_janken == 0 and i == 5:
                print('|                                          　/￣￣￣ /##                                             |')
                print('|                                          /  /￣/　/ ________                                       |')
                print("|                                        ー'　_/　/ |________|                                       |")
                print('|                                           /___ノ　                                                 |')
            if katimake_count == 0 and enemy_janken == 1 and i == 5:
                print('|                                    　＿ノ￣/       　  ＿/￣/_　                                   |')
                print('|                                    /＿　　∠_         /__　　＿/                                    |')
                print('|                                   /＿　　＿_/ 二二| /__　　＿_/                                    |')
                print('|                                  　/＿/      二二|   /＿/ 　　                                     |')
            if katimake_count == 0 and enemy_janken == 2 and i == 5:
                print("|                                   　   / ７' ７ ロ                                                 |")
                print('|                                  　   /　/i　l 　  ________                                        |')
                print('|                                    _ノ　/  i　 i_ |________|                                       |')
                print('|                                   /__,／　　ゝ､__|                                                 |')
            if katimake_count == 0 and i == 10:
                print('|              　  -┼- 　  ┼　 、　 -┼─　 　|　-┼                                                    |')
                print('|               　 ,-┼/-、 /　 | ヽ  / -─ 　|　 |　                                                  |')
                print('|              　ヽ__ﾚ　ノ 　 dヽ　 / ヽ___ し  dヽ                                                  |')
            if katimake_count == 0 and select_hand == 0 and i == 16:
                print("|      　/￣￣￣ /##                                                                                 |")
                print('|      /  /￣/　/ ________                                                                           |')
                print("|     ー'　_/　/ |________|                                                                          |")
                print('|　     /___ノ　                                                                                     |')
            if katimake_count == 0 and select_hand == 1 and i == 16:
                print("|      　                         　＿ノ￣/       　  ＿/￣/_　                                      |")
                print('|                                /＿　　∠_         /__　　＿/                                        |')
                print("|                               /＿　　＿_/ 二二| /__　　＿_/                                        |")
                print('|　          　                 　/＿/      二二|   /＿/ 　　                                        |')
            if katimake_count == 0 and select_hand== 2 and i == 16:
                print("|                                                                 　  / ７' ７ ロ                    |")
                print('|                                                               　   /　/i　l 　  ________           |')
                print("|                                                                 _ノ　/ i　 i_  |________|          |")
                print('|　                                                     　　      /__,／　　ゝ､__|                   |')
            if enemy_janken != select_hand and katimake_count == 1 and i == 5:
                print('|　                 -┼- 　  ┼　 、　 -┼─　 　 ,--t-、                                                |')
                print('|　                ,-┼/-、 /　 | ヽ  / -─ 　i　/　 |                                                 |')
                print('|               　ヽ__ﾚ　ノ 　 dヽ　 / ヽ___  V　　ノ                                                |')
            if katimake_count == 1 and i == 10:
                if enemy_janken == select_hand:
                    for i in range(3):
                        print('|',end='')
                        print(' '*100,end='')
                        print('|')
                    print('|　        -┼- 　 i　 　 、 .ー--、                                                                  |')
                    print('|　       ,-┼/-、 |　　　ヽ  ,　　　                                                                 |')
                    print("|　      ヽ__ﾚ　ノ ヽ/　　'  ヽ＿＿                                                                  |")
                    aiko = 1
                if enemy_janken == 0 and select_hand == 1:
                    print('|          -┼- i　-┼-                                                                                |')
                    print('|          -┼- |　　|                                                                                |')
                    print('|          α^ヽ `　ノ　                                                                              |')
                if enemy_janken == 0 and select_hand == 2:
                    print('|          -┼、＼-┼─ 　                                                                              |')
                    print('|          /　|　 レ--、                                                                             |')
                    print('|         /　ノ 　 ＿ノ                                                                              |')
                if enemy_janken == 1 and select_hand == 0:
                    print('|          -┼、＼-┼─ 　                                                                              |')
                    print('|          /　|　 レ--、                                                                             |')
                    print('|         /　ノ 　 ＿ノ                                                                              |')
                if enemy_janken == 1 and select_hand == 2:
                    print('|          -┼- i　-┼-                                                                                |')
                    print('|          -┼- |　　|                                                                                |')
                    print('|          α^ヽ `　ノ　                                                                              |')
                if enemy_janken == 2 and select_hand == 0:
                    print('|          -┼- i　-┼-                                                                                |')
                    print('|          -┼- |　　|                                                                                |')
                    print('|          α^ヽ `　ノ　                                                                              |')
                if enemy_janken == 2 and select_hand == 1:
                    print('|          -┼、＼-┼─ 　                                                                              |')
                    print('|          /　|　 レ--、                                                                             |')
                    print('|         /　ノ 　 ＿ノ                                                                              |')
                for i in range(5):
                    print('|',end='')
                    print(' '*100,end='')
                    print('|')
            if i == 17:
                print('|                                          ---スペース---                                            |')
            print('|',end='')
            print(' '*100,end='')
            print('|')
        print('+',end='')
        print('-'*100,end='')
        print('+')
        if katimake_count == 1 and aiko == 0:
            readchar.readchar()
            break
        katimake_count = 1
        readchar.readchar()
        os.system('clear')
        if aiko == 1:
            select_hand = saisyoha()
            os.system('clear')
            aiko = 0
            katimake_count = 0
            enemy_janken = random.randint(0,2)
#     while True:
#         print('+',end='')
#         print('-'*100,end='')
#         print('+')
#         for i in range(30):
#             if i == 10:

#             print('|',end='')
#             print(' '*100,end='')
#             print('|')
#         print('+',end='')
#         print('-'*100,end='')
#         print('+')
janken()
# ＿＿　  ＿＿　##  i　-┼- -┼- ─┼-   -┼、＼ /￣\
# 　 　ヽ 　 　ヽ  |　　|  -┼-  α  　/　|　    /
# 　 ＿ﾉ　   ＿ﾉ   `　ノ　 α^ヽ ノ ./　 J     d
