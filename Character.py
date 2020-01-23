class Character():
	def __init__(self,c):
		self._centre = (c[0],c[1])
		self._health = c[2]

	def reduce_health(self):
		self._health = self._health - 1

	def get_centre(self):
		return self._centre

	def get_health(self):
		return self._health