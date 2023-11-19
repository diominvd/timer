import customtkinter as ctk


class View(ctk.CTk):
	def __init__(self):
		super().__init__()

		# Configure View
		self.title("TomatoTimer")
		self.geometry("220x300")

		# TabView -> view
		self.tabview = ctk.CTkTabview(self)
		self.tabview.add("Timer")
		self.tabview.add("Settings")

		# Widgets -> TabView -> Tab:"Timer"
		self.time_label = ctk.CTkLabel(self.tabview.tab("Timer"))
		self.timer_option_menu = ctk.CTkOptionMenu(self.tabview.tab("Timer"))
		self.start_timer_button = ctk.CTkButton(self.tabview.tab('Timer'))
		self.pause_timer_butoon = ctk.CTkButton(self.tabview.tab("Timer"))
		self.reset_timer_button = ctk.CTkButton(self.tabview.tab("Timer"))

		# Place widgets
		self.cinfigure_tab1_widgets()
		self.palace_tab1_widgets()

	def cinfigure_tab1_widgets(self) -> None:
		# TabView:
		self.tabview._segmented_button._buttons_dict["Timer"].configure(font=("Calibri", 14)) # TabView:Tab:Timer
		self.tabview._segmented_button._buttons_dict["Settings"].configure(font=("Calibri", 14)) # TabView:Tab:Settings
		# Label:
		self.time_label.configure(font=("Calibri", 30, "bold"), text="TIME:TEXT")
		# OptionMenu:
		self.timer_option_menu.configure(font=("Calibri", 14), values=["work".title(), "break".title()], command=None)
		self.timer_option_menu.set("work".title())
		# Buttons:
		self.start_timer_button.configure(font=("Calibri", 14), text="Start", command=None)
		self.pause_timer_butoon.configure(font=("Calibri", 14), text="Pause", command=None)
		self.reset_timer_button.configure(font=("Calibri", 14), text="Reset", command=None)

	def palace_tab1_widgets(self) -> None:
		self.tabview.pack(expand=True, fill="both")
		self.time_label.pack(padx=0, pady=15)
		self.timer_option_menu.pack(padx=0, pady=5)
		self.start_timer_button.pack(padx=0, pady=5)
		self.pause_timer_butoon.pack(padx=0, pady=5)
		self.reset_timer_button.pack(padx=0, pady=5)
