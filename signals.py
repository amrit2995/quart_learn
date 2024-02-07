from quart import Quart,request_finished
from quart.signals import signals_available

app = Quart(__name__)
def finished(sender, response, **extra):
    print("About to send a Response")
    print(response)

request_finished.connect(finished)
@app.route("/api")
async def my_microservice():
    response = {"Hello":"world"}
    return response

if __name__ == "__main__":
    app.run(port=7000)