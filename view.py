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
		self.settings_time_label = ctk.CTkLabel(self.tabview.tab("Settings"))
		self.settings_timer_option_menu = ctk.CTkOptionMenu(self.tabview.tab("Settings"))
		self.settings_edit_button = ctk.CTkButton(self.tabview.tab("Settings"))
		self.settings_save_button = ctk.CTkButton(self.tabview.tab("Settings"))

		# Place widgets
		self.configure_tab1_widgets()
		self.configure_tab2_widgets()
		self.palace_tab1_widgets()
		self.place_tab2_widgets()

	def configure_tab1_widgets(self) -> None:
		# TabView:
		self.tabview._segmented_button._buttons_dict["Timer"].configure(font=("Calibri", 14)) # TabView:Tab:Timer
		self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)
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
		self.settings_timer_option_menu.configure(font=("Calibri", 14, "bold"), values=["work".title(), "break".title()], command=None)
		self.settings_timer_option_menu.set("work".title())
		# Label:
		self.settings_time_label.configure(font=("Calibri", 30), text="TIME")
		self.settings_time_label.bind("<MouseWheel>", self.settings_time_label_scroll_handler)
		# Buttons
		self.settings_edit_button.configure(font=("Calibri", 14), text="Save")
		self.settings_save_button.configure(font=("Calibri", 14), text="Edit")

	def palace_tab1_widgets(self) -> None:
		self.tabview.pack(expand=True, fill="both")
		self.time_label.pack(padx=0, pady=15)
		self.timer_option_menu.pack(padx=0, pady=5)
		self.start_timer_button.pack(padx=0, pady=5)
		self.pause_timer_butoon.pack(padx=0, pady=5)
		self.reset_timer_button.pack(padx=0, pady=5)

	def place_tab2_widgets(self) -> None:
		self.settings_time_label.grid(row=0, column=0, padx=0, pady=0)
		self.settings_timer_option_menu.grid(row=1, column=0, padx=0, pady=0)
		self.settings_edit_button.grid(row=2, column=0, padx=0, pady=0)
		self.settings_save_button.grid(row=3, column=0, padx=0, pady=0)

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

	def settings_time_label_scroll_handler(self, event) -> None:
		self.controller.settings_time_label_scroll_event(event)
