import customtkinter as ctk


class UI():
	def __init__(self):
		self.PADX: int = 5
		self.PADY: int = 5
		self.FONT_BUTTONS: str = "Fredoka"
		self.CLR_ACCENT_1: str = "#00a5ff"
		self.CLR_ACCENT_2: str = "#008fdb"
		self.CLR_ACCENT_3: str = "#0077b8"
		self.CLR_DISABLED: str = "#66b9e6"
		self.CLR_BUTTON_TEXT_NORMAL: str = "#fcfcfc"
		self.CLR_BUTTON_TEXT_DISABLED: str = "#dadada"

		ctk.FontManager.load_font("src/BakbakOne-Regular.ttf")
		ctk.FontManager.load_font("src/Fredoka-Regular.ttf")


class View(ctk.CTk):
	def __init__(self, controller):
		super().__init__()
		self.ui = UI()
		# Connect controller
		self.controller = controller

		# Configure View
		self.title("TomatoTimer")
		self.geometry("220x310")

		# TabView -> view
		self.tabview = ctk.CTkTabview(self)
		self.tabview.add("Timer")
		self.tabview.add("Settings")

		# Configure TabView
		self.tabview.configure(segmented_button_selected_color=self.ui.CLR_ACCENT_1, segmented_button_selected_hover_color=self.ui.CLR_ACCENT_2)

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
		self.settings_cancel_button = ctk.CTkButton(self.tabview.tab("Settings"))
		self.settings_hint_label = ctk.CTkLabel(self.tabview.tab('Settings'))

		# Place widgets
		self.configure_tab1_widgets()
		self.configure_tab2_widgets()
		self.palace_tab1_widgets()
		self.place_tab2_widgets()

	def configure_tab1_widgets(self) -> None:
		# TabView:
		self.tabview._segmented_button._buttons_dict["Timer"].configure(font=(self.ui.FONT_BUTTONS, 12)) # TabView:Tab:Timer
		# Label:
		self.time_label.configure(font=("Bakbak One", 40, "bold"), text=None)
		# OptionMenu:
		self.timer_option_menu.configure(font=(self.ui.FONT_BUTTONS, 14, "normal"), fg_color=self.ui.CLR_ACCENT_1, button_color=self.ui.CLR_ACCENT_2, button_hover_color=self.ui.CLR_ACCENT_3, values=["work".title(), "break".title()], command=self.timer_option_menu_choice_handler)
		self.timer_option_menu.set("work".title())
		# Buttons:
		self.start_timer_button.configure(state="normal", font=(self.ui.FONT_BUTTONS, 14), text="Start", text_color=self.ui.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.ui.CLR_BUTTON_TEXT_DISABLED, fg_color=self.ui.CLR_ACCENT_1, hover_color=self.ui.CLR_ACCENT_3,  command=self.start_timer_button_click_handler)
		self.pause_timer_butoon.configure(state="disabled", font=(self.ui.FONT_BUTTONS, 14), text="Pause", text_color=self.ui.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.ui.CLR_BUTTON_TEXT_DISABLED, fg_color=self.ui.CLR_DISABLED, hover_color=self.ui.CLR_ACCENT_3,  command=self.pause_timer_button_click_handler)
		self.reset_timer_button.configure(state="disabled", font=(self.ui.FONT_BUTTONS, 14), text="Reset", text_color=self.ui.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.ui.CLR_BUTTON_TEXT_DISABLED, fg_color=self.ui.CLR_DISABLED, hover_color=self.ui.CLR_ACCENT_3,  command=self.reset_timer_button_click_handler)

	def configure_tab2_widgets(self) -> None:
		# TabView:
		self.tabview._segmented_button._buttons_dict["Settings"].configure(font=(self.ui.FONT_BUTTONS, 12)) # TabView:Tab:Settings
		# OptionMenu:
		self.settings_timer_option_menu.configure(font=(self.ui.FONT_BUTTONS, 14), fg_color=self.ui.CLR_ACCENT_1, button_color=self.ui.CLR_ACCENT_2, button_hover_color=self.ui.CLR_ACCENT_3, values=["work".title(), "break".title()], command=self.settings_timer_option_menu_choice_handler)
		self.settings_timer_option_menu.set("work".title())
		# Label:
		self.settings_time_label.configure(font=("Bakbak One", 40, "bold"), text=None)
		self.settings_time_label.bind("<MouseWheel>", None)
		self.settings_hint_label.configure(font=(self.ui.FONT_BUTTONS, 13), text_color=self.ui.CLR_BUTTON_TEXT_NORMAL, text="Scroll label to edit")
		# Buttons
		self.settings_edit_button.configure(state="normal", font=(self.ui.FONT_BUTTONS, 14), text="Edit", text_color=self.ui.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.ui.CLR_BUTTON_TEXT_DISABLED, fg_color=self.ui.CLR_ACCENT_1, hover_color=self.ui.CLR_ACCENT_3,   command=self.settings_edit_button_click_handler)
		self.settings_save_button.configure(state="disabled", font=(self.ui.FONT_BUTTONS, 14), text="Save", text_color=self.ui.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.ui.CLR_BUTTON_TEXT_DISABLED, fg_color=self.ui.CLR_DISABLED, hover_color=self.ui.CLR_ACCENT_3,   command=self.settings_save_button_click_handler)
		self.settings_cancel_button.configure(state="normal", font=(self.ui.FONT_BUTTONS, 14), text="Cancel", text_color=self.ui.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.ui.CLR_BUTTON_TEXT_DISABLED, fg_color=self.ui.CLR_ACCENT_1, hover_color=self.ui.CLR_ACCENT_3,  command=self.settings_cancel_button_click_handler)

	def palace_tab1_widgets(self) -> None:
		self.tabview.pack(expand=True, fill="both")
		self.time_label.pack(padx=0, pady=self.ui.PADY*2)
		self.timer_option_menu.pack(padx=0, pady=self.ui.PADY)
		self.start_timer_button.pack(padx=0, pady=self.ui.PADY)
		self.pause_timer_butoon.pack(padx=0, pady=self.ui.PADY)
		self.reset_timer_button.pack(padx=0, pady=self.ui.PADY)

	def place_tab2_widgets(self) -> None:
		self.settings_time_label.pack(padx=0, pady=self.ui.PADY*2)
		self.settings_timer_option_menu.pack(padx=0, pady=self.ui.PADY)
		self.settings_edit_button.pack(padx=0, pady=self.ui.PADY)
		self.settings_save_button.pack(padx=0, pady=self.ui.PADY)

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

	def settings_timer_option_menu_choice_handler(self, choice) -> None:
		self.controller.settings_timer_option_menu_event()

	def settings_edit_button_click_handler(self) -> None:
		self.controller.settings_edit_button_event()

	def settings_save_button_click_handler(self) -> None:
		self.controller.settings_save_button_event()

	def settings_cancel_button_click_handler(self) -> None:
		self.controller.settings_cancel_button_event()
