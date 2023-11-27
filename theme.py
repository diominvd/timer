import customtkinter as ctk
import sys
import os


class Theme:
	def __init__(self, CLR_ACCENT_0, CLR_ACCENT_1, CLR_ACCENT_2, CLR_ACCENT_3, CLR_TEXT, CLR_BUTTON_TEXT_NORMAL, CLR_BUTTON_TEXT_DISABLED):
		# Default options
		self.PADX: int = 5
		self.PADY: int = 5
		self.FONT_TEXT: str = "Staatliches"
		self.FONT_TIMER: str = "Bakbak One"

		# Colors
		self.CLR_ACCENT_0: str = CLR_ACCENT_0
		self.CLR_ACCENT_1: str = CLR_ACCENT_1
		self.CLR_ACCENT_2: str = CLR_ACCENT_2
		self.CLR_ACCENT_3: str = CLR_ACCENT_3
		self.CLR_TEXT: str = CLR_TEXT
		self.CLR_BUTTON_TEXT_NORMAL: str = CLR_BUTTON_TEXT_NORMAL
		self.CLR_BUTTON_TEXT_DISABLED: str = CLR_BUTTON_TEXT_DISABLED

		# Load fonts
		ctk.FontManager.load_font(self.resource_path("src/BakbakOne-Regular.ttf"))
		ctk.FontManager.load_font(self.resource_path("src/Staatliches-Regular.ttf"))

	def resource_path(self, relative_path):
	    """ Get absolute path to resource, works for dev and for PyInstaller """
	    try:
	        # PyInstaller creates a temp folder and stores path in _MEIPASS
	        base_path = sys._MEIPASS
	    except Exception:
	        base_path = os.path.abspath(".")

	    return os.path.join(base_path, relative_path)
