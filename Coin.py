from Gamescreen import Gamescreen
import numpy as np

class Coin():

    def __init__(self):
        self.__loc = []
        self.__timer = 0
        self.__coin = 'o'

    def create(self,n,sc):
        if self.__timer % 13 == 0 and sc.get_trip() != 2:
            r = int(np.random.randint(low = 2,high = 4,size = 1))
            for i in range(r):
                self.__loc.append((n , 239 + i))

    def update(self,sc):
        s = []

        for i in range(len(self.__loc)):
            if self.__loc[i][1] >= 0:
                self.__loc[i] = (self.__loc[i][0] , self.__loc[i][1] - sc.get_speed())
            else:
                s.append(self.__loc[i])

        for i in s:
            self.__loc.remove(i)

        self.printer(sc)
        self.__timer = self.__timer + 1

    def printer(self,sc):
        for i in range(len(self.__loc)):
            if self.__loc[i][0] > 0 and self.__loc[i][0] < 54:
                if self.__loc[i][1] > 0 and self.__loc[i][1] < 238 and self.__loc[i][1] >= 0:
                    sc.set(self.__loc[i][0],self.__loc[i][1],self.__coin)

    def rem(self,c):
        score =  0
        for i in range(4):
            for j in range(4):
                if (i,j) not in [(0,0),(0,3),(3,0),(3,3)]:
                    if (c[0] + i,c[1] + j) in self.__loc: 
                        score = score + 1
                        self.__loc.remove((c[0] + i,c[1] + j))

        return score

    def clear_coin(self):
        if len(self.__loc) == 0:
            return True
        return False

    def random_location(self):
        return int(np.random.randint(low = 10,high = 45,size = 1))