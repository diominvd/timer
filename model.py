class Model:
	def __init__(self, mode: str):
		# Configure timer
		self.mode: str = mode
		self.id: str = None
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

	def change_model_status(self, key: str) -> bool:
		match key:
			case "start":
				self.status = True
			case "pause":
				if self.status:
					self.status = False
				elif not self.status:
					self.status = True
			case "reset":
				self.status = False
		return self.status
