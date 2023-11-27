import json
import os
import theme


class Data:
	def __init__(self):
		os.system("mkdir data")
		self.create_data_file()
		self.create_themes_file()

	def resource_path(self, relative_path):
	    """ Get absolute path to resource, works for dev and for PyInstaller """
	    try:
	        # PyInstaller creates a temp folder and stores path in _MEIPASS
	        base_path = sys._MEIPASS
	    except Exception:
	        base_path = os.path.abspath(".")

	    return os.path.join(base_path, relative_path)

	def create_data_file(self) -> None:
		if os.path.isfile("data/data.json"):
			pass
		else:
			file = open("data/data.json", "w")
			data: dict = {"work": {"hours": 0, "minutes": 45, "seconds": 0}, "break": {"hours": 0, "minutes": 5, "seconds": 0}}
			json.dump(data, file, indent=4)

	def create_themes_file(self) -> None:
		if os.path.isfile("data/themes.json"):
			pass
		else:
			file = open("data/themes.json", "w")
			data: dict = {"themes": {"lime": ["#daff73", "#c2ff1c", "#ace219", "#99c916", "#ffffff", "#383838", "#4e4e4e"], "cyan": ["#b0fffc", "#00fff6", "#00d6ce", "#00b3ad", "#ffffff", "#383838", "#4e4e4e"], "ocean": ["#6eabff", "#006aff", "#005ad7", "#004cb6", "#ffffff", "#383838", "#4e4e4e"], "red": ["#ff6c9d", "#ff0055", "#d10046", "#a80038", "#ffffff", "#383838", "#4e4e4e"], "orange": ["#ffbb80", "#ff7700", "#da6600", "#ba5700", "#ffffff", "#383838", "#4e4e4e"]}, "current_theme": "cyan"}
			json.dump(data, file, indent=4)

	def load_themes(self) -> dict:
		with open("data/themes.json", "r") as file:
			themes: dict = json.load(file)["themes"]
			file.close()
		# Create themes
		themes: dict = {
			"lime": theme.Theme(*themes["lime"][:7]),
			"cyan": theme.Theme(*themes["cyan"][:7]),
			"ocean": theme.Theme(*themes["ocean"][:7]),
			"red": theme.Theme(*themes["red"][:7]),
			"orange": theme.Theme(*themes["orange"][:7]),
		}
		return themes

	def load_current_theme(self) -> str:
		with open("data/themes.json", "r") as file:
			theme: str = json.load(file)["current_theme"]
			file.close()
			return theme

	def fix_theme(self, choice) -> None:
		with open("data/themes.json", "r") as file:
			data: dict = json.load(file)
			file.close()
		data["current_theme"] = choice.lower()
		with open("data/themes.json", "w") as file:
			json.dump(data, file, indent=4)
			file.close()

	def data_analysis(self, data: dict, key: str) -> dict:
		hours: int = data[key]["hours"]
		minutes: int = data[key]["minutes"]
		seconds: int = data[key]["seconds"]
		hours += minutes // 60
		minutes = minutes - (60 * (minutes // 60))
		return {"hours": hours, "minutes": minutes, "seconds": seconds}

	def load_data(self, key=None) -> dict:
		with open("data/data.json", "r") as file:
			data: dict = json.load(file) # Whole data
			file.close()
		match key:
			case "work":
				return self.data_analysis(data=data, key=key) # Work data
			case "break":
				return self.data_analysis(data=data, key=key) # Break data
			case None:
				return data
			case _:
				raise ValueError("Incorrect key value: ('work' or 'break')")

	# data = {hours: n, minutes: n, seconds: n}
	def extract_data(self, data: dict) -> tuple:
		return data["hours"], data["minutes"], data["seconds"]

	def write_data(self, data: dict) -> None:
		with open("data/data.json", "w") as file:
			json.dump(data, file, indent=4)
			file.close()
			