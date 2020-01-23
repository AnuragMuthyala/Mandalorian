from Gamescreen import Gamescreen
from colorama import Back,Fore

class Background():

    def __init__(self):

        with open("mountain") as mountain:
            self.__body1 = mountain.readlines()

        with open("town") as town:
            self.__body2 = town.readlines()

        self.__centre = 115
        self.__scene_number = 1
        self.__cloud = [[] for i in range(4)]
        self.__mountain = [[] for i in range(len(self.__body1))]
        self.__town = [[] for i in range(len(self.__body2))]
        self.__ground = 'T'
        self.__cloud[0] = [' ',' ',' ',' ',' ','_','_','_','_',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.__cloud[1] = [' ',' ',' ','_','(',' ',' ',' ',' ',')','_','_','_','_',' ',' ',' ',' ']
        self.__cloud[2] = [' ','_','(',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',')','_','_',' ']
        self.__cloud[3] = ['(','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',')']

        self.remove_mountain()
        self.remove_town()

        self.__scene_centre = [(54 - len(self.__mountain) + 2,239),(54 - len(self.__town) + 2,239)]

    def remove_mountain(self):
        for i in range(len(self.__body1)):
            for j in range(len(self.__body1[i])):
                self.__mountain[i].extend(self.__body1[i][j])
            if '\n' in self.__mountain[i]:
                self.__mountain[i].remove('\n')

    def remove_town(self):
        for i in range(len(self.__body2)):
            for j in range(len(self.__body2[i])):
                self.__town[i].extend(self.__body2[i][j])
            if '\n' in self.__town[i]:
                self.__town[i].remove('\n')

    def update(self,sc):

        if self.__centre < 92:
            self.__centre = 114

        for i in range(self.__centre,-23,-23):
            self.printer((1,i),sc)

        for i in range(self.__centre,238,23):
            self.printer((1,i),sc)

        for i in range(238):
            sc.set(53,i,self.__ground)
        self.__centre = self.__centre - sc.get_speed()

        self.scene_update(sc)

    def printer(self,c,sc):
        
        for i in range(4):
            for j in range(18):

                if c[0] + i >= 0 and c[1] + j >= 0 and c[0] + i < 54 and c[1] + j < 238:
                    sc.set(c[0] + i,c[1] + j,self.__cloud[i][j])

    def mountain_printer(self,sc):
        for i in range(len(self.__mountain)):
            for j in range(len(self.__mountain[i])):
                if self.__scene_centre[0][0] + i < 54 and self.__scene_centre[0][1] + j < 238 and self.__scene_centre[0][1] + j >= 0:
                    sc.set(self.__scene_centre[0][0] + i,self.__scene_centre[0][1] + j,self.__mountain[i][j])

    def mountain_update(self,sc):
        self.__scene_centre[0] = (self.__scene_centre[0][0],self.__scene_centre[0][1] - sc.get_speed())
        if self.__scene_centre[0][1] < -98:
            self.__scene_number = 2
            self.__scene_centre[0] = (54 - len(self.__mountain) + 2,239)
        else:
            self.mountain_printer(sc)

    def town_printer(self,sc):
        for i in range(len(self.__town)):
            for j in range(len(self.__town[i])):
                if self.__scene_centre[1][0] + i < 54 and self.__scene_centre[1][1] + j < 238 and self.__scene_centre[1][1] + j >= 0:
                    sc.set(self.__scene_centre[1][0] + i,self.__scene_centre[1][1] + j,self.__town[i][j])

    def town_update(self,sc):
        self.__scene_centre[1] = (self.__scene_centre[1][0],self.__scene_centre[1][1] - sc.get_speed())
        if self.__scene_centre[1][1] < -56:
            self.__scene_number = 1
            self.__scene_centre[1] = (54 - len(self.__town) + 2,239)
        else:
            self.town_printer(sc)

    def scene_update(self,sc):
        if self.__scene_number == 1:
            self.mountain_update(sc)
        elif self.__scene_number == 2:
            self.town_update(sc)