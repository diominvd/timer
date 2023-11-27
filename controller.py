import pygame


class Controller:
	def __init__(self, data, model, view):
		# Connect data, model, view
		self.data = data
		self.model = model
		self.view = view
		
		pygame.mixer.init()
		self.load_timer_time()
		self.load_settings_timer_time()
		self.update_time_label()
		self.update_settings_time_label()

	def set_theme(self) -> None:
		self.view.theme: str = self.data.load_themes()[self.data.load_current_theme()]
		self.view.configure_widgets_colors()
		return None

	def load_timer_time(self) -> None:
		data: dict = self.data.load_data(key=self.view.timer_option_menu.get().lower())
		time: tuple = self.data.extract_data(data=data)
		self.model.hours, self.model.minutes, self.model.seconds = time

	def load_settings_timer_time(self) -> None:
		data: dict = self.data.load_data(key=self.view.settings_timer_option_menu.get().lower())
		time: tuple = self.data.extract_data(data=data)
		self.model.settings_hours, self.model.settings_minutes, self.model.settings_seconds = time

	def update_time_label(self) -> None:
		# Format time for output it to time_label
		hours: str = f"0{self.model.hours}" if self.model.hours < 10 else f"{self.model.hours}"
		minutes: str = f"0{self.model.minutes}" if self.model.minutes < 10 else f"{self.model.minutes}"
		seconds: str = f"0{self.model.seconds}" if self.model.seconds < 10 else f"{self.model.seconds}"
		time = f"{minutes}:{seconds}" if self.model.hours == 0 else f"{hours}:{minutes}:{seconds}"
		# Configure view:time_label
		self.view.time_label.configure(text=time)

	def update_settings_time_label(self) -> None:
		# Format time for output it to settings_time_label
		hours: str = f"0{self.model.settings_hours}" if self.model.settings_hours < 10 else f"{self.model.settings_hours}"
		minutes: str = f"0{self.model.settings_minutes}" if self.model.settings_minutes < 10 else f"{self.model.settings_minutes}"
		seconds: str = f"0{self.model.settings_seconds}" if self.model.settings_seconds < 10 else f"{self.model.settings_seconds}"
		time = f"{minutes}:{seconds}" if self.model.settings_hours == 0 else f"{hours}:{minutes}:{seconds}"
		# Configure view:time_label
		self.view.settings_time_label.configure(text=time)

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
		self.view.start_timer_button.configure(state="disabled", fg_color=self.view.theme.CLR_ACCENT_0)
		self.view.pause_timer_butoon.configure(state="normal", fg_color=self.view.theme.CLR_ACCENT_1)
		self.view.reset_timer_button.configure(state="normal", fg_color=self.view.theme.CLR_ACCENT_1)
		self.model.change_model_status(key="start")
		self.update_timer()

	def update_timer(self) -> None:
		if self.model.status:
			# Check end of timer
			if (self.model.hours, self.model.minutes, self.model.seconds) == (0, 0, 0):
				self.model.status = False
				self.view.after_cancel(self.model.id) # Stop model.count()
				pygame.mixer.music.load("src/notify.mp3")
				pygame.mixer.music.play(loops=0)
				self.model.create_notify(mode=self.model.mode)
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
		self.view.start_timer_button.configure(state="normal", fg_color=self.view.theme.CLR_ACCENT_1)
		self.view.pause_timer_butoon.configure(state="disabled", fg_color=self.view.theme.CLR_ACCENT_0)
		self.view.reset_timer_button.configure(state="disabled", fg_color=self.view.theme.CLR_ACCENT_0)
		# Configure pause_button:text
		self.view.pause_timer_butoon.configure(text="Pause")
		# Stop update_timer
		try:
			self.view.after_cancel(self.model.id)
		except ValueError:
			pass
		finally:
			self.model.id = None
			self.load_timer_time()
			self.update_time_label()

	def settings_time_label_scroll_event(self, event) -> None:
		self.model.count_settings(event)
		mode: str = self.view.settings_timer_option_menu.get().lower()
		data: dict = {
			f"{mode}": 
				{
					"hours": self.model.settings_hours,
					"minutes": self.model.settings_minutes,
					"seconds": self.model.settings_seconds
				}
			}
		time: dict = self.data.data_analysis(data=data, key=mode)
		self.model.settings_hours, self.model.settings_minutes, self.model.settings_seconds = tuple(time.values())
		self.update_settings_time_label()

	def settings_timer_option_menu_event(self) -> None:
		self.view.settings_time_label.unbind("<MouseWheel>")
		self.view.settings_edit_button.configure(state="normal", text="Edit", fg_color=self.view.theme.CLR_ACCENT_1, command=self.view.settings_edit_button_click_handler)
		self.view.settings_cancel_button.configure(state="disabled", text_color=self.view.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.view.theme.CLR_ACCENT_0)
		self.load_settings_timer_time()
		self.update_settings_time_label()

	def settings_edit_button_event(self) -> None:
		self.view.settings_time_label.bind("<MouseWheel>", self.view.settings_time_label_scroll_handler)
		self.view.settings_edit_button.configure(text="Save", text_color=self.view.theme.CLR_BUTTON_TEXT_NORMAL, command=self.view.settings_save_button_click_handler)
		self.view.settings_cancel_button.configure(state="normal", text_color=self.view.theme.CLR_BUTTON_TEXT_NORMAL, fg_color=self.view.theme.CLR_ACCENT_1)

	def settings_save_button_event(self) -> None:
		mode: str = self.view.settings_timer_option_menu.get().lower()
		data: dict = self.data.load_data() # Return all data
		data[mode]["hours"] = self.model.settings_hours
		data[mode]["minutes"] = self.model.settings_minutes
		data[mode]["seconds"] = self.model.settings_seconds
		self.data.write_data(data)
		# Configure view
		self.view.settings_time_label.unbind("<MouseWheel>")
		self.view.settings_edit_button.configure(text="Edit", text_color=self.view.theme.CLR_BUTTON_TEXT_NORMAL, command=self.view.settings_edit_button_click_handler)
		self.view.settings_cancel_button.configure(state="disabled", text_color=self.view.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.view.theme.CLR_ACCENT_0)
		self.load_settings_timer_time()
		self.update_settings_time_label()
		# Check timer status
		if self.model.status:
			pass
		else:
			self.load_timer_time()
			self.update_time_label()

	def settings_cancel_button_event(self) -> None:
		self.view.settings_time_label.unbind("<MouseWheel>")
		self.view.settings_edit_button.configure(text="Edit", text_color=self.view.theme.CLR_BUTTON_TEXT_NORMAL, command=self.view.settings_edit_button_click_handler)
		self.view.settings_cancel_button.configure(state="disabled", text_color=self.view.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.view.theme.CLR_ACCENT_0)
		self.load_settings_timer_time()
		self.update_settings_time_label()

	def settings_theme_option_menu_event(self, choice) -> None:
		self.data.fix_theme(choice)
		self.set_theme()
		return None