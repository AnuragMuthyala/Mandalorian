from colorama import Fore
from os import system
from time import sleep

import math


class Gamescreen():
    def __init__(self):
        self.__grid = [[' ' for i in range(238)] for i in range(54)]
        self.__speed = 1
        self.__speed_time = -1
        self.__health = -1
        self.__trip = 0
        self.__boss = -1
        self.__game_time = 150
        self.__shield_status = False
        self.__score = 0
        self.__nxt = 0
        self.__timer = 0
        self.__no = 0
        self.__m_no = 0
        self.__s_no = 0
        self.__disappeared = 0
        self.__beams = 21
        self.__empty = []
        self.__store = []
        self.__field = []
        self.__coin_loc = -1
        self.__end = 0

    def set(self,y,x,shape):
        self.__grid[y][x] = shape

    def print_screen(self):
        if self.__end == 0:
            self.__game_time = self.__game_time - 0.0625
        self.print_bar()

        for i in range(54):
            if i < 7:
                print(Fore.WHITE + ''.join(self.__grid[i]))
            elif i == 53:
                print(Fore.GREEN + ''.join(self.__grid[i]))
            else:
                if self.__shield_status == False:
                    print(Fore.CYAN + ''.join(self.__grid[i]))
                else:
                    print(Fore.YELLOW + ''.join(self.__grid[i]))


    def refresh(self):
        self.__grid = [[' ' for i in range(238)] for i in range(54)]

    def boost_time(self):
        self.__speed = 3
        self.__speed_time = 0

    def get_speed(self):
        return self.__speed

    def speed_timer(self):
        if self.__speed_time == -1:
            return 0
        else:
            if self.__speed_time >= 8:
                self.__speed = 1
                self.__speed_time = -1
            else:
                self.__speed_time = self.__speed_time + 0.0625

    def set_trip(self):
        self.__trip = self.__trip + 1

    def get_trip(self):
        return self.__trip

    def set_shield(self,s):
        self.__shield_status = s

    def add(self,s):
        self.__score = self.__score + s

    def set_health(self,s):
        self.__health = s

    def bar(self,n,l):
        for i in range(len(l)):
            self.__grid[0][n + i] = l[i]

    def set_boss(self,s):
        self.__boss = s

    def set_nxt(self,s):
        self.__nxt = s

    def set_timer(self,s):
        self.__timer = s

    def inc_timer(self):
        self.__timer = self.__timer + 1

    def set_no(self,s):
        self.__no = s

    def inc_no(self):
        self.__no = self.__no + 1

    def set_m_no(self,s):
        self.__m_no = s

    def set_s_no(self,s):
        self.__s_no = s

    def set_disappeared(self,s):
        self.__disappeared = s

    def inc_disappeared(self):
        self.__disappeared = self.__disappeared + 1

    def init_field(self):
        self.__field = []

    def get_field(self):
        return self.__field

    def set_field(self,s):
        self.__field.append(s)

    def get_nxt(self):
        return self.__nxt

    def get_timer(self):
        return self.__timer 

    def get_no(self):
        return self.__no

    def get_m_no(self):
        return self.__m_no

    def get_s_no(self):
        return self.__s_no

    def get_disappeared(self):
        return self.__disappeared

    def get_beams(self):
        return self.__beams

    def add_trash(self,s):
        self.__store.append(s)

    def get_trash(self):
        return self.__store

    def add_empty(self,s):
        self.__store.extend(s)

    def get_empty(self):
        return self.__empty

    def init_trash(self):
        self.__store = []

    def init_empty(self):
        self.__empty = [] 

    def set_coin_loc(self,s):
        self.__coin_loc = s

    def get_coin_loc(self):
        return self.__coin_loc

    def print_bar(self):

        n = 0
        l = 'SCORE:'.split()

        self.bar(n,l)

        n = 6
        l = str(self.__score).split()

        self.bar(n,l)

        n = 15
        l = 'TIME:'.split()

        self.bar(n,l)

        n = 20
        l = str(math.ceil(self.__game_time)).split()

        self.bar(n,l)

        n = 30 
        l = 'HEALTH:'.split()

        self.bar(n,l)

        n = 37
        l = ['#' for i in range(self.__health + 1)]

        self.bar(n,l)

        if self.__boss != -1:

            n = 170
            l = 'BOSS:'.split()

            self.bar(n,l)

            n = 175
            l = ['#' for i in range(self.__boss)]

            self.bar(n,l)

    def cut(self):
        self.__end = 1
        for i in range(119):
            for j in range(54):
                self.__grid[j][i] = ' '
                self.__grid[j][237 - i] = ' '

            self.print_screen()
            sleep(0.0625)
            system('clear')

    def congratulate(self):
        
        i = 0
        msg = 'Congratulations!!!'
        msg2 = 'Your_Score_is_' + str(self.__score)

        l = msg.split()

        while i < 28:
            for j in range(len(l)):
                self.refresh()
                self.__grid[i][110 + j] = l[j]
                self.print_screen()
                sleep(0.0625)
                system('clear')
            i = i + 1

        l2 = msg2.split()

        for j in range(len(l2)):
            self.__grid[i + 3][111 + j] = l2[j]
        self.print_screen()

        sleep(5)

