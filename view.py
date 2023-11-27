import customtkinter as ctk


class View(ctk.CTk):
	def __init__(self, controller, data):
		super().__init__()
		# Connect data
		self.data = data
		# Connect controller
		self.controller = controller

		# Themes
		self.theme: str = self.data.load_themes()[data.load_current_theme()]

		# Configure View
		self.title("TomatoTimer")
		self.geometry("220x360")
		self.resizable(width=False, height=False)
		ctk.set_appearance_mode("dark")

		# TabView -> view
		self.tabview = ctk.CTkTabview(self)
		self.tabview.add("  Timer  ")
		self.tabview.tab("  Timer  ").grid_columnconfigure(0, weight=1)
		self.tabview.add("  Settings  ")
		self.tabview.tab("  Settings  ").grid_columnconfigure(0, weight=1)
		self.tabview.pack(expand=True, fill="both")

		# Widgets -> Tab:"Timer" -> TabView
		self.time_label = ctk.CTkLabel(self.tabview.tab("  Timer  "))
		self.timer_option_menu = ctk.CTkOptionMenu(self.tabview.tab("  Timer  "))
		self.start_timer_button = ctk.CTkButton(self.tabview.tab("  Timer  "))
		self.pause_timer_butoon = ctk.CTkButton(self.tabview.tab("  Timer  "))
		self.reset_timer_button = ctk.CTkButton(self.tabview.tab("  Timer  "))

		# Widgets -> Tab:"Settings" -> TabView
		self.settings_time_label = ctk.CTkLabel(self.tabview.tab("  Settings  "))
		self.settings_timer_option_menu = ctk.CTkOptionMenu(self.tabview.tab("  Settings  "))
		self.settings_edit_button = ctk.CTkButton(self.tabview.tab("  Settings  "))
		self.settings_save_button = ctk.CTkButton(self.tabview.tab("  Settings  "))
		self.settings_cancel_button = ctk.CTkButton(self.tabview.tab("  Settings  "))
		self.settings_theme_label = ctk.CTkLabel(self.tabview.tab("  Settings  "))
		self.settings_theme_option_menu = ctk.CTkOptionMenu(self.tabview.tab("  Settings  "))

		# Place widgets
		self.configure_tab1_widgets()
		self.configure_tab2_widgets()
		self.configure_widgets_colors()
		self.palace_tab1_widgets()
		self.place_tab2_widgets()

	def configure_tab1_widgets(self) -> None:
		# TabView:
		self.tabview._segmented_button._buttons_dict["  Timer  "].configure(font=(self.theme.FONT_TEXT, 12))
		# OptionMenu:
		self.timer_option_menu.configure(font=(self.theme.FONT_TEXT, 14, "normal"), values=["work".title(), "break".title()], command=self.timer_option_menu_choice_handler)
		self.timer_option_menu.set("work".title())
		# Label:
		self.time_label.configure(font=(self.theme.FONT_TIMER, 40, "bold"), text=None)
		# Buttons:
		self.start_timer_button.configure(state="normal", font=(self.theme.FONT_TEXT, 14), text="START", command=self.start_timer_button_click_handler)
		self.pause_timer_butoon.configure(state="disabled", font=(self.theme.FONT_TEXT, 14), text="Pause", command=self.pause_timer_button_click_handler)
		self.reset_timer_button.configure(state="disabled", font=(self.theme.FONT_TEXT, 14), text="Reset", command=self.reset_timer_button_click_handler)

	def configure_tab2_widgets(self) -> None:
		# TabView:
		self.tabview._segmented_button._buttons_dict["  Settings  "].configure(font=(self.theme.FONT_TEXT, 12)) # TabView:Tab:Settings
		# OptionMenu:
		self.settings_timer_option_menu.configure(font=(self.theme.FONT_TEXT, 14), values=["work".title(), "break".title()], command=self.settings_timer_option_menu_choice_handler)
		self.settings_timer_option_menu.set("work".title())
		self.settings_theme_option_menu.configure(font=(self.theme.FONT_TEXT, 14), values=[theme_name.title() for theme_name in self.data.load_themes().keys()], command=self.settings_theme_option_menu_choice_handler)
		self.settings_theme_option_menu.set(self.data.load_current_theme().title())
		# Label:
		self.settings_time_label.configure(font=("Bakbak One", 40, "bold"), text=None)
		self.settings_time_label.bind("<MouseWheel>", None)
		self.settings_theme_label.configure(font=(self.theme.FONT_TEXT, 14), text="Theme settings")
		# Buttons
		self.settings_edit_button.configure(state="normal", font=(self.theme.FONT_TEXT, 14), text="Edit", command=self.settings_edit_button_click_handler)
		self.settings_save_button.configure(state="disabled", font=(self.theme.FONT_TEXT, 14), text="Save", command=self.settings_save_button_click_handler)
		self.settings_cancel_button.configure(state="normal", font=(self.theme.FONT_TEXT, 14), text="Cancel", command=self.settings_cancel_button_click_handler)

	def configure_widgets_colors(self) -> None:
		# TabView
		self.tabview.configure(segmented_button_selected_color=self.theme.CLR_ACCENT_1, segmented_button_selected_hover_color=self.theme.CLR_ACCENT_2)
		# Tab "Timer"
		self.tabview._segmented_button._buttons_dict["  Timer  "].configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL)
		self.time_label.configure(text_color=self.theme.CLR_TEXT)
		self.timer_option_menu.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, fg_color=self.theme.CLR_ACCENT_1, button_color=self.theme.CLR_ACCENT_2, button_hover_color=self.theme.CLR_ACCENT_3)
		self.start_timer_button.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.theme.CLR_ACCENT_1, hover_color=self.theme.CLR_ACCENT_3)
		self.pause_timer_butoon.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.theme.CLR_ACCENT_0, hover_color=self.theme.CLR_ACCENT_3)
		self.reset_timer_button.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.theme.CLR_ACCENT_0, hover_color=self.theme.CLR_ACCENT_3)
		# Tab "Settings"
		self.tabview._segmented_button._buttons_dict["  Settings  "].configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL) # TabView:Tab:Settings
		self.settings_time_label.configure(text_color=self.theme.CLR_TEXT)
		self.settings_timer_option_menu.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, fg_color=self.theme.CLR_ACCENT_1, button_color=self.theme.CLR_ACCENT_2, button_hover_color=self.theme.CLR_ACCENT_3)
		self.settings_edit_button.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.theme.CLR_ACCENT_1, hover_color=self.theme.CLR_ACCENT_3)
		self.settings_save_button.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.theme.CLR_ACCENT_0, hover_color=self.theme.CLR_ACCENT_3)
		self.settings_cancel_button.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, text_color_disabled=self.theme.CLR_BUTTON_TEXT_DISABLED, fg_color=self.theme.CLR_ACCENT_1, hover_color=self.theme.CLR_ACCENT_3)
		self.settings_theme_label.configure(text_color=self.theme.CLR_TEXT)
		self.settings_theme_option_menu.configure(text_color=self.theme.CLR_BUTTON_TEXT_NORMAL, fg_color=self.theme.CLR_ACCENT_1, button_color=self.theme.CLR_ACCENT_2, button_hover_color=self.theme.CLR_ACCENT_3)

	def palace_tab1_widgets(self) -> None:
		self.time_label.grid(column=0, row=0, padx=0, pady=self.theme.PADY*2)
		self.timer_option_menu.grid(column=0, row=1, padx=0, pady=self.theme.PADY)
		self.start_timer_button.grid(column=0, row=2, padx=0, pady=self.theme.PADY)
		self.pause_timer_butoon.grid(column=0, row=3, padx=0, pady=self.theme.PADY)
		self.reset_timer_button.grid(column=0, row=4, padx=0, pady=self.theme.PADY)

	def place_tab2_widgets(self) -> None:
		self.settings_time_label.grid(row=0, column=0, padx=0, pady=self.theme.PADY*2)
		self.settings_timer_option_menu.grid(row=1, column=0, padx=0, pady=self.theme.PADY)
		self.settings_edit_button.grid(row=2, column=0, padx=0, pady=self.theme.PADY)
		self.settings_save_button.grid(row=3, column=0, padx=0, pady=self.theme.PADY)
		self.settings_theme_label.grid(row=5, column=0, padx=0, pady=(self.theme.PADY*2, 0))
		self.settings_theme_option_menu.grid(row=6, column=0, padx=0, pady=self.theme.PADY)

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

	def settings_theme_option_menu_choice_handler(self, choice) -> None:
		self.controller.settings_theme_option_menu_event(choice)