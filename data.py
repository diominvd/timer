import json


class Data:
	def __init__(self):
		pass

	def load_data(self, key=None) -> dict:
		with open("data.json", "r") as file:
			data: dict = json.load(file)
		match key:
			case "work":
				return data["work"]
			case "break":
				return data["break"]
			case None:
				return data
			case _:
				return data

	# data = {hours: n, minutes: n, seconds: n}
	def extract_data(self, data: dict) -> tuple:
		return (data["hours"], data["minutes"], data["seconds"])
		