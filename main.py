from controller import Controller
from data import Data
from model import Model
from view import View

data = Data()
model = Model(mode="work")
app = View(controller=None)
controller = Controller(data=data, model=model, view=app)
# Add controller to view
app.controller = controller


if __name__ == "__main__":
	app.mainloop()
	