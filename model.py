class Model:
	def __init__(self, mode: str):
		# Configure timer
		self.id: str = None
		self.mode: str = mode
		self.status: bool = False
		self.hours: int = None
		self.minutes: int = None
		self.seconds: int = None
