from Gamescreen import Gamescreen
import numpy as np
from Obstacle import Obstacle

class Beam(Obstacle):

    def __init__(self):

        super().__init__(int(np.random.randint(low = 10 , high = 43 , size = 1)))
        self.__length = int(np.random.randint(low = 8 , high = 11 , size = 1))
        self.__proj = 'x'
        self.__beam = '+'
        self.__orient = np.random.randint(low = 1,high = 4,size = 1)
        self._immersed = 0
        
    def print_beam(self,sc):
        if self.__orient == 1:
            for i in range(self.__length):
                if self._centre[0] + 1 + i < 54 and self._centre[1] < 238 and self._centre[1] >= 0:
                    sc.set(self._centre[0] + 1 + i,self._centre[1],self.__beam)

        elif self.__orient == 2:
            for i in range(self.__length):
                if self._centre[0] < 54 and self._centre[1] + 1 + i < 238 and self._centre[1] + i + 1 >= 0:
                    sc.set(self._centre[0],self._centre[1] + 1 + i,self.__beam)

        elif self.__orient == 3:
            for i in range(self.__length):
                if self._centre[0] + i + 1 < 54 and self._centre[1] + 1 + i < 238 and self._centre[1] + i + 1 >= 0:
                    sc.set(self._centre[0] + i + 1,self._centre[1] + i + 1,self.__beam)

    def print_proj(self,sc):

        if self.__orient == 1:
            if self._centre[0] < 54 and self._centre[1] < 238 and self._centre[1]>= 0:
                sc.set(self._centre[0],self._centre[1],self.__proj)
            if self._centre[0] + self.__length + 1 < 54 and self._centre[1] < 238 and self._centre[1] >= 0:
                sc.set(self._centre[0] + self.__length + 1,self._centre[1],self.__proj)
                self._immersed = 1

        elif self.__orient == 2:
            if self._centre[0] < 54 and self._centre[1] < 238 and self._centre[1] >= 0:
                sc.set(self._centre[0],self._centre[1],self.__proj)
            if self._centre[0] < 54 and self._centre[1] + self.__length + 1 < 238 and self._centre[1] + self.__length + 1 >= 0:
                sc.set(self._centre[0],self._centre[1] + self.__length + 1,self.__proj)
                self._immersed = 1

        elif self.__orient == 3:
            if self._centre[0] < 54 and self._centre[1] < 238 and self._centre[1] >= 0:
                sc.set(self._centre[0],self._centre[1],self.__proj)
            if self._centre[0] + self.__length + 1 < 54 and self._centre[1] + self.__length + 1 < 238 and self._centre[1] + self.__length + 1 >= 0:
                sc.set(self._centre[0] + self.__length + 1,self._centre[1] + self.__length + 1,self.__proj)
                self._immersed = 1

    def update(self,sc):
        
        if self._centre[1] < 0:
            if self.__orient == 1 and self._centre[1] < 0:
                return 0
            if (self.__orient == 2 or self.__orient == 3) and self._centre[1] + self.__length + 1 < 0:
                return 0
            self.print_beam(sc)
            self.print_proj(sc)
            
        else:
            self.print_beam(sc)
            self.print_proj(sc)
        self._centre = (self._centre[0],self._centre[1] - sc.get_speed())
        return 1

    def check_collision(self,c):

        for i in range(4):
            for j in range(4):
                if (c[0]+i,c[1]+j) not in [(0,0),(0,3),(3,0),(3,3)]:
                    if self.__orient == 1:
                        if c[0] + i >= self._centre[0] and c[0] + i <= self._centre[0] + self.__length + 1 and c[1] + j == self._centre[1]:
                            return True
                    elif self.__orient == 2:
                        if c[1] + j >= self._centre[1] and c[1] + j <= self._centre[1] + self.__length + 1 and c[0] + i == self._centre[0]:
                            return True
                    elif self.__orient == 3:
                        if c[0] + i >= self._centre[0] and c[0] + i <= self._centre[0] + self.__length + 1 and c[1] + j == self._centre[1] + (c[0] - self._centre[0]):
                            return True
        return False

    def check_bullets(self,bl):

        for b in bl:
            if self.__orient == 1:
                if b[0] >= self._centre[0] and b[0] < self._centre[0] + self.__length  + 2 and b[1] >= self._centre[1]:
                    return b

            elif self.__orient == 2:
                if b[0] == self._centre[0] and b[1] >= self._centre[1]:
                    return b

            elif self.__orient == 3:
                if b[0] >= self._centre[0] and b[0] < self._centre[0] + self.__length + 2 and b[1] >= self._centre[1] + (b[0] - self._centre[0]):
                    return b

        return -1

    def check_location(self,n):
        if self.__orient == 1 and (n < self._centre[0] or n > self._centre[0] + self.__length):
            return 1
        elif self.__orient == 2 and n != self._centre[0]:
            return 1
        elif self.__orient == 3 and (n < self._centre[0] or n > self._centre[0] + self.__length):
            return 1
        else:
            return -1