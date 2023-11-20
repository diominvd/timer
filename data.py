import json


class Data:
	def __init__(self):
		pass

	def load_data(self, key=None) -> dict:
		with open("data.json", "r") as file:
			data: dict = json.load(file) # Whole data
		match key:
			case "work":
				return self.data_analysis(data=data, key=key) # Work data
			case "break":
				return self.data_analysis(data=data, key=key) # Break data
			case None:
				return data
			case _:
				raise ValueError("Incorrect key value: ('work' or 'break')")

	def data_analysis(self, data: dict, key: str) -> None:
		hours: int = data[key]["hours"]
		minutes: int = data[key]["minutes"]
		seconds: int = data[key]["seconds"]
		hours += minutes // 60
		minutes = minutes - (60 * (minutes // 60))
		return {"hours": hours, "minutes": minutes, "seconds": seconds}


	# data = {hours: n, minutes: n, seconds: n}
	def extract_data(self, data: dict) -> tuple:
		return data["hours"], data["minutes"], data["seconds"]
		