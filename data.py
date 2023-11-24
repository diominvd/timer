import json
import os

class Data:
	def __init__(self):
		self.create_data_file()

	def create_data_file(self) -> None:
		if os.path.isfile("data.json"):
			pass
		else:
			file = open("data.json", "w")
			data: dict = {"work": {"hours": 0, "minutes": 45, "seconds": 0}, "break": {"hours": 0, "minutes": 5, "seconds": 0}}
			json.dump(data, file, indent=4)

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

	def data_analysis(self, data: dict, key: str) -> dict:
		hours: int = data[key]["hours"]
		minutes: int = data[key]["minutes"]
		seconds: int = data[key]["seconds"]
		hours += minutes // 60
		minutes = minutes - (60 * (minutes // 60))
		return {"hours": hours, "minutes": minutes, "seconds": seconds}


	# data = {hours: n, minutes: n, seconds: n}
	def extract_data(self, data: dict) -> tuple:
		return data["hours"], data["minutes"], data["seconds"]

	def write_data(self, data: dict) -> None:
		with open("data.json", "w") as file:
			json.dump(data, file, indent=4)
			file.close()
