from Gamescreen import Gamescreen
import numpy as np
from Obstacle import Obstacle

class Magnet(Obstacle):
    def __init__(self):
        super().__init__(int(np.random.randint(low = 10,high = 45,size = 1)))
        self.__length = 5
        self.__magnet = [[] for i in range(4)]
        self.__magnet[0] = ['<','|','~','~',' ']
        self.__magnet[1] = ['<','|',' ','~','~']
        self.__magnet[2] = ['<','|',' ','~','~']
        self.__magnet[3] = ['<','|','~','~',' ']

    def update(self,sc):
        if self._centre[1] + self.__length < 0:
            return 0

        else:
            self.print_magnet(sc)
            if self._centre[1] < 234:
                self._immersed = 1
            self._centre = (self._centre[0],self._centre[1] - sc.get_speed())

    def print_magnet(self,sc):
        for i in range(len(self.__magnet)):
            for j in range(self.__length):

                if self._centre[0] + i >= 0 and self._centre[1] + j >= 0 and self._centre[0] + i < 54 and self._centre[1] + j < 238:
                    sc.set(self._centre[0] + i,self._centre[1] + j,self.__magnet[i][j])

    def attract(self):
        return self._centre

    def check_collision(self,c):
        for i in range(4):
            for j in range(4):
                if (c[0]+i,c[1]+j) not in [(0,0),(0,3),(3,0),(3,3)]:
                    if c[0] + i >= self._centre[0] and c[0] + i < self._centre[0] + len(self.__magnet):
                        if c[1] + j >= self._centre[1] and self._centre[1] + self.__length:
                            return True
        return False

    def check_bullets(self,bl):
        s = []
        for i in range(len(self.__magnet)):
            for j in range(self.__length):
                for b in bl:
                    if b[0] >= self._centre[0] and b[0] < self._centre[0] + len(self.__magnet):
                        if b[1] >= self._centre[1] and b[1] < self._centre[1] + self.__length:
                            s.append(b)

        return s