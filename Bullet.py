from Gamescreen import Gamescreen

class Bullet():
    def __init__(self):
        self.__centre = []
        self.__bullet = 'D'

    def travel(self):
        store = []
        for i in range(len(self.__centre)):
            self.__centre[i] = (self.__centre[i][0] , self.__centre[i][1] + 3)
            if self.__centre[i][1] > 237:
                store.append(self.__centre[i])

        for i in store:
            self.__centre.remove(i)

    def new_bullet(self,c):
        self.__centre.append(c)

    def update(self,sc):
        self.travel()
        for i in range(len(self.__centre)):
            sc.set(self.__centre[i][0],self.__centre[i][1],self.__bullet)

    def erase(self,t):
        if t in self.__centre:
            self.__centre.remove(t)

    def get_centre(self):
        return self.__centre