from QuorAPI.HTMLparser import get_answer, get_profile

class User():
	def __init__(self, username):
		self.username = username
		self.followers = self._followers()
	def answers(self, num=1000):
		pass
	def questions(self, answered=True, num=1000):
		pass
	def _followers(self):
		pass

	@staticmethod
	def followers(self):
		return self.followers
