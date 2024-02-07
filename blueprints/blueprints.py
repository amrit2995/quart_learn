from quart import Quart
from teams import teams

app = Quart(__name__)
app.register_blueprint(teams)

if __name__ == "__main__":
    app.run(port=8001)