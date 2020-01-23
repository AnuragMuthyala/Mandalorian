from Gamescreen import Gamescreen
from Character import Character

class Boss(Character):
    def __init__(self):
        super().__init__((8,239,10))
        self.__timer = 0
        self.__boss = [[] for i in range(5)]
        with open("boss") as boss:
            self.__body = boss.readlines()
        self.remove_line()

    def breath(self):
        if self.__timer % 12 == 0:
            self.__timer = self.__timer + 1
            return True
        self.__timer = self.__timer + 1
        return False

    def remove_line(self):
        for i in range(len(self.__body)):
            for j in range(len(self.__body[i])):
                self.__boss[i].extend(self.__body[i][j])
            if '\n' in self.__boss[i]:
                self.__boss[i].remove('\n')

    def printer(self,sc):
        for i in range(5):
            for j in range(len(self.__boss[i])):
                if self._centre[0] + i < 54 and self._centre[1] + j < 238:
                    sc.set(self._centre[0] + i,self._centre[1] + j,self.__boss[i][j])

    def entrance(self):
        self._centre = (self._centre[0] , self._centre[1] - 1)

    def in_range(self):
        if self._centre[1] == 215:
            return True
        return False

    def move(self,c):
        
        if c[0] > self._centre[0]:
            self._centre = (self._centre[0] + 1,self._centre[1])
        elif c[0] < self._centre[0]:
            self._centre = (self._centre[0] - 1,self._centre[1])

    def damage(self,bl):
        s = []

        for i in range(len(bl)):
            if self.body_touch(bl[i]) == True:
                self.reduce_health()
                s.append(i)

        return s

    def reduce_health(self):
        if self._health <= 0:
            return 0

        else:
            self._health = self._health - 1

    def body_touch(self,t):
        if t[0] >= self._centre[0] and t[0] < self._centre[0] + 5 and t[1] > 215:
            return True

        return False


    def not_dead(self):
        if self._health > 0:
            return True
        return False