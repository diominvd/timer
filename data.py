import json
import os
import theme


class Data:
	def __init__(self):
		self.create_data_file()

	def create_data_file(self) -> None:
		if os.path.isfile("data.json"):
			pass
		else:
			file = open("data.json", "w")
			data: dict = {"timer": {"work": {"hours": 0, "minutes": 45, "seconds": 0}, "break": {"hours": 0, "minutes": 5, "seconds": 0}}, "theme": {"current_theme": "green"}}
			json.dump(data, file, indent=4)

	def load_themes(self) -> dict:
		with open("themes.json", "r") as file:
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
		with open("themes.json", "r") as file:
			theme: str = json.load(file)["current_theme"]
			file.close()
			return theme

	def fix_theme(self, choice) -> None:
		with open("themes.json", "r") as file:
			data: dict = json.load(file)
			file.close()
		data["current_theme"] = choice.lower()
		with open("themes.json", "w") as file:
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
		with open("data.json", "r") as file:
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
		with open("data.json", "w") as file:
			json.dump(data, file, indent=4)
			file.close()
			