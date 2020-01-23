from Gamescreen import Gamescreen

class Obstacle():

    def __init__(self,n):
        self._centre = (n , 239)
        self._immersed = 0

    def get_immersed(self):
        return self._immersed

    def update(self,sc):
    	self._centre = (self._centre[0],self._centre - 1)