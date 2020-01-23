from Gamescreen import Gamescreen
from Character import Character

import sys
import select
import tty
import termios
import numpy as np

class User(Character):

    def __init__(self):
        super().__init__((46,10,4))
        self.__old = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        self.__gravity = 1
        self.__time = 0
        self.__shield = False
        self.__shield_timer = 60
        self.__shield_active_time = 0
        self.__body = [[] for i in range(4)]
        self.__body[0] = [' ','-','-',' ']
        self.__body[1] = [' ','[','\\',' ']
        self.__body[2] = ['H','|','|','=']
        self.__body[3] = [' ','>','>',' ']

    def get_settings(self):
        return self.__old

    def isData(self):
        return select.select([sys.stdin], [], [], 0.01) == ([sys.stdin], [], [])

    def shoot(self):
        return (self._centre[0] + 2,self._centre[1] + 4)

    def fall(self):
        if self.__time > 6:
            self.__gravity = 2

        self._centre = (self._centre[0] + self.__gravity , self._centre[1])
        if self._centre[0] > 49:
            self._centre = (49 , self._centre[1])
        self.__time = self.__time + 1

    def move(self,timeout = 0.01):

        while True:
            if self.isData():
                char = sys.stdin.read(1)
                
                if char == 'w':
                    self.__gravity = 1
                    self.__time = 0
                    self._centre = (self._centre[0] - 2 , self._centre[1])
                    if self._centre[0] < 7:
                        self._centre = (7 , self._centre[1])
                    return 1

                else:
                    if char == 'a':
                        if self._centre[1] > 0:
                            self._centre = (self._centre[0] , self._centre[1] - 1)

                    elif char == 'd':
                        if self._centre[1] < 234:
                            self._centre = (self._centre[0] , self._centre[1] + 1)

                    elif char == 'b':
                        return self.shoot()

                    elif char == ' ':
                        if self.__shield_timer >= 60:
                            self.__shield = True
                            self.__shield_active_time = 10
                            self.__shield_timer = 0

                    elif char == 'q':
                        print("GoodBye!!!")
                        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.__old)
                        quit()
                        
                return 0
            else:
                return 0

    def printer(self,sc):
        for i in range(4):
            for j in range(4):
                sc.set(self._centre[0] + i,self._centre[1] + j,self.__body[i][j])

    def reduce_health(self):
        if self._health <= 0:
            print("Better Luck Next Time!")
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.__old)
            quit()

        else:
            self._health = self._health - 1

    def in_range(self,field):
        for f in field:
            if self._centre[1] < f[1]:
                if self._centre[0] >= f[0] and self._centre[0] < f[0] + 4:
                    return True
        return False

    def attraction(self):
        if self._centre[1] < 234:
            self._centre = (self._centre[0] , self._centre[1] + 1)

    def body_touch(self,t):
        for i in range(len(self.__body)):
            for j in range(len(self.__body[i])):
                if t[0] == self._centre[0] + i and (t[1] == self._centre[1] + j or t[1] == self._centre[1] + j + 1) and self.__body[i][j] != ' ':
                    return True

        return False

    def damage(self,bl):
        s = []

        for b in bl:
            if self.body_touch(b) == True:
                s.append(b)

        return s

    def get_shield(self):
        return self.__shield

    def shield_duration(self):
        if self.__shield_active_time <= 0:
            self.__shield = False
        else:
            self.__shield_active_time = self.__shield_active_time - 0.0625

    def shield_recover(self):
        self.__shield_timer = self.__shield_timer + 0.0625