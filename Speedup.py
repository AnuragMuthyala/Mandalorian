from Gamescreen import Gamescreen
import numpy as np

class Speedup():
    def __init__(self):
        self.__l = (int(np.random.randint(low = 10,high = 45,size = 1)),239)
        self.__shape = '$'

    def update(self):
        self.__l = (self.__l[0] , self.__l[1] - 1)

    def display(self,sc):
        if self.__l[1] < 238:
            sc.set(self.__l[0],self.__l[1],self.__shape)

    def activate(self,c):
        if self.__l[0] >= c[0] and self.__l[0] < c[0] + 4:
            if self.__l[1] >= c[1] and self.__l[1] < c[1] + 4:
                return True
        return False

    def in_screen(self):
        if self.__l[1] < 0:
            return False
        return True