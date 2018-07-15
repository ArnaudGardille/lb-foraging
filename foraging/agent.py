import numpy as np
import logging
_MAX_INT = 999999

class Agent:

	name = "Prototype Agent"

	def __repr__(self):
		return self.name

	def __init__(self, position, level):
		self.logger = logging.getLogger(__name__)
		self.visibility = _MAX_INT
		self.position = position
		self.level = level
		self.score = 0

	def step(self, obs):
		raise NotImplemented("You must implement an agent")

	def _closest_food(self, obs, max_food_level=0):
		x, y = self.position
		field = np.copy(obs.field)

		if max_food_level > 0:
			field[field > max_food_level] = 0

		r, c = np.nonzero(field)
		try:
			min_idx = ((r - x) ** 2 + (c - y) ** 2).argmin()
		except ValueError:
			return None

		return r[min_idx], c[min_idx]