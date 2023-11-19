from controller import Controller
from model import Model
from view import View


model = Model()
controller = Controller()
app = View(model, controller)


if __name__ == "__main__":
	app.mainloop()