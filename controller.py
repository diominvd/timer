class Controller:
	def __init__(self, data, model, view):
		# Connect data, model, view
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

	def timer_option_menu_event(self, choice: str) -> str:
		match choice:
			case "Work":
				self.model.mode = "work"
			case "Break":
				self.model.mode = "break"
		# Update timer
		self.reset_timer()
		return self.model.mode

	def start_timer_button_event(self) -> None:
		# Configure timer buttons:state
		self.view.start_timer_button.configure(state="disabled")
		self.view.pause_timer_butoon.configure(state="normal")
		self.view.reset_timer_button.configure(state="normal")
		self.model.change_model_status(key="start")
		self.update_timer()

	def update_timer(self) -> None:
		if self.model.status:
			# Check end of timer
			if (self.model.hours, self.model.minutes, self.model.seconds) == (0, 0, 0):
				self.model.status = False
				self.view.after_cancel(self.model.id) # Stop model.count()
				return None
			else:
				self.model.count()
			self.update_time_label()
		self.model.id = self.view.after(1000, self.update_timer) ### Test time value / default = 1000

	def pause_timer_button_event(self) -> None:
		self.model.change_model_status(key="pause")
		self.pause_timer()

	def pause_timer(self) -> None:
		text = "Pause" if self.model.status == True else "Resume"
		# Configure pause_button:text
		self.view.pause_timer_butoon.configure(text=text)

	def reset_timer_button_event(self) -> None:
		self.model.change_model_status(key="reset")
		self.reset_timer()

	def reset_timer(self) -> None:
		# Configure timer buttons:state
		self.view.start_timer_button.configure(state="normal")
		self.view.pause_timer_butoon.configure(state="disabled")
		self.view.reset_timer_button.configure(state="disabled")
		# Configure pause_button:text
		self.view.pause_timer_butoon.configure(text="Pause")
		# Stop update_timer
		try:
			self.view.after_cancel(self.model.id)
		except ValueError:
			pass
		finally:
			self.model.id = None
			self.load_time()
			self.update_time_label()
