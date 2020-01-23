from Gamescreen import Gamescreen

class Iceball():
    def __init__(self):
        self.__loc = []
        self.__shape = ['<','>']

    def travel(self):
        store = []
        for i in range(len(self.__loc)):
            self.__loc[i] = (self.__loc[i][0] , self.__loc[i][1] - 3)
            if self.__loc[i][1] < 0:
                store.append(self.__loc[i])

        for i in store:
            self.__loc.remove(i)

    def new_iceball(self,c):
        self.__loc.append((c[0] + 3,c[1] - 1))

    def update(self,sc):
        self.travel()
        for i in range(len(self.__loc)):
            for j in range(len(self.__shape)):
                if self.__loc[i][1] < 215:
                    sc.set(self.__loc[i][0],self.__loc[i][1] + j,self.__shape[j])

    def erase(self,t):
        if t in self.__loc:
            self.__loc.remove(t)

    def get_loc(self):
        return self.__loc