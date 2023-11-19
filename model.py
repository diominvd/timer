class Model:
	def __init__(self, mode: str):
		# Configure timer
		self.id: str = None
		self.mode: str = mode
		self.status: bool = False
		self.hours: int = None
		self.minutes: int = None
		self.seconds: int = None

	def count(self) -> None:
		if self.seconds == 0:
			if self.minutes == 0:
				self.hours -= 1
				self.minutes = 59
				self.seconds = 59
			else:
				self.minutes -= 1
				self.seconds = 59
		else:
			self.seconds -= 1

	def start(self) -> None:
		self.status = True