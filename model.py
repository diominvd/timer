from plyer import notification


class Model:
	def __init__(self, mode: str):
		# Configure timer
		self.mode: str = mode
		self.id: str = None
		self.status: bool = False
		self.hours: int = None
		self.minutes: int = None
		self.seconds: int = None
		self.settings_hours: int = None
		self.settings_minutes: int = None
		self.settings_seconds: int = None

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

	def count_settings(self, event) -> None:
		match event.delta:
			case 120:
				self.settings_minutes += 1
			case -120:
				# Check time limit
				if self.settings_hours == 0 and self.settings_minutes == 1:
					pass
				else:
					self.settings_minutes -= 1

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

	def create_notify(self, mode) -> None:
		title: str = f"{mode.title()} is over"
		match mode:
			case "work":
				message: str = f"Time to take a break!"
			case "break":
				message: str = "It's time to get to work!"
		notification.notify(title=title, message=message, app_name="Tomato Timer", app_icon=None, timeout=10, toast=False)