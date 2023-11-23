import customtkinter as ctk


class View(ctk.CTk):
	def __init__(self, controller):
		super().__init__()
		# Connect controller
		self.controller = controller

		# Configure View
		self.title("TomatoTimer")
		self.geometry("220x300")

		# TabView -> view
		self.tabview = ctk.CTkTabview(self)
		self.tabview.add("Timer")
		self.tabview.add("Settings")

		# Widgets -> Tab:"Timer" -> TabView
		self.time_label = ctk.CTkLabel(self.tabview.tab("Timer"))
		self.timer_option_menu = ctk.CTkOptionMenu(self.tabview.tab("Timer"))
		self.start_timer_button = ctk.CTkButton(self.tabview.tab('Timer'))
		self.pause_timer_butoon = ctk.CTkButton(self.tabview.tab("Timer"))
		self.reset_timer_button = ctk.CTkButton(self.tabview.tab("Timer"))

		# Widgets -> Tab:"Settings" -> TabView
		self.settings_timer_option_menu = ctk.CTkOptionMenu(self.tabview.tab("Settings"))
		self.minutes_label = ctk.CTkLabel(self.tabview.tab("Settings"))
		self.minutes_entry = ctk.CTkEntry(self.tabview.tab("Settings"))
		self.seconds_label = ctk.CTkLabel(self.tabview.tab("Settings"))
		self.seconds_entry = ctk.CTkEntry(self.tabview.tab("Settings"))
		self.edit_button = ctk.CTkButton(self.tabview.tab("Settings"))
		self.save_button = ctk.CTkButton(self.tabview.tab("Settings"))

		# Place widgets
		self.configure_tab1_widgets()
		self.configure_tab2_widgets()
		self.palace_tab1_widgets()
		self.place_tab2_widgets()

	def configure_tab1_widgets(self) -> None:
		# TabView:
		self.tabview._segmented_button._buttons_dict["Timer"].configure(font=("Calibri", 14)) # TabView:Tab:Timer
		# Label:
		self.time_label.configure(font=("Calibri", 30, "bold"), text=None)
		# OptionMenu:
		self.timer_option_menu.configure(font=("Calibri", 14), values=["work".title(), "break".title()], command=self.timer_option_menu_choice_handler)
		self.timer_option_menu.set("work".title())
		# Buttons:
		self.start_timer_button.configure(state="normal", font=("Calibri", 14), text="Start", command=self.start_timer_button_click_handler)
		self.pause_timer_butoon.configure(state="disabled", font=("Calibri", 14), text="Pause", command=self.pause_timer_button_click_handler)
		self.reset_timer_button.configure(state="disabled", font=("Calibri", 14), text="Reset", command=self.reset_timer_button_click_handler)

	def configure_tab2_widgets(self) -> None:
		# TabView:
		self.tabview._segmented_button._buttons_dict["Settings"].configure(font=("Calibri", 14)) # TabView:Tab:Settings
		# OptionMenu:
		self.settings_timer_option_menu.configure(font=("Calibri", 14), values=["work".title(), "break".title()], command=None)
		self.settings_timer_option_menu.set("work".title())
		# Label:
		self.minutes_label.configure(font=("Calibri", 14), text="Minutes:")
		self.seconds_label.configure(font=("Calibri", 14), text="Seconds:")
		# Entry
		self.minutes_entry.configure(font=("Calibri", 14))
		self.seconds_entry.configure(font=("Calibri", 14))
		# Buttons
		self.edit_button.configure(font=("Calibri", 14), text="Save")
		self.save_button.configure(font=("Calibri", 14), text="Edit")

	def palace_tab1_widgets(self) -> None:
		self.tabview.pack(expand=True, fill="both")
		self.time_label.pack(padx=0, pady=15)
		self.timer_option_menu.pack(padx=0, pady=5)
		self.start_timer_button.pack(padx=0, pady=5)
		self.pause_timer_butoon.pack(padx=0, pady=5)
		self.reset_timer_button.pack(padx=0, pady=5)

	def place_tab2_widgets(self) -> None:
		self.settings_timer_option_menu.grid(row=0, column=0, columnspan=2, padx=0, pady=0)
		self.minutes_label.grid(row=1, column=0, padx=0, pady=0)
		self.minutes_entry.grid(row=1, column=1, padx=0, pady=0)
		self.seconds_label.grid(row=2, column=0, padx=0, pady=0)
		self.seconds_entry.grid(row=2, column=1, padx=0, pady=0)
		self.edit_button.grid(row=3, column=0, columnspan=2, padx=0, pady=0)
		self.save_button.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

	def timer_option_menu_choice_handler(self, choice) -> None:
		#  Call choice event
		self.controller.timer_option_menu_event(choice)

	def start_timer_button_click_handler(self) -> None:
		# Call start event
		self.controller.start_timer_button_event()

	def pause_timer_button_click_handler(self) -> None:
		# Call pause event
		self.controller.pause_timer_button_event()

	def reset_timer_button_click_handler(self) -> None:
		# Call reset event
		self.controller.reset_timer_button_event()
