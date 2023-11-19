from controller import Controller
from data import Data
from model import Model
from view import View

data = Data()
model = Model(mode="work")
app = View()
controller = Controller(data=data, model=model, view=app)


if __name__ == "__main__":
	app.mainloop()