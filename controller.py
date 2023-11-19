class Controller:
	def __init__(self, data, model, view):
		self.data = data
		self.model = model
		self.view = view

		self.load_time()
		self.update_time_label()

	def load_time(self) -> None:
		data: dict = self.data.load_data(key=self.model.mode)
		time: tuple = self.data.extract_data(data=data)
		self.model.hours, self.model.minutes, self.model.seconds = time
		
	def update_time_label(self) -> None:
		# Format time for output it to time_label
		hours: str = f"0{self.model.hours}" if self.model.hours < 10 else f"{self.model.hours}"
		minutes: str = f"0{self.model.minutes}" if self.model.minutes < 10 else f"{self.model.minutes}"
		seconds: str = f"0{self.model.seconds}" if self.model.seconds < 10 else f"{self.model.seconds}"
		time = f"{minutes}:{seconds}" if self.model.hours == 0 else f"{hours}:{minutes}:{seconds}"
		# Configure view:time_label
		self.view.time_label.configure(text=time)