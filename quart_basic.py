from quart import Quart, request, jsonify, g
from quart.signals import signals_available

app = Quart(__name__)

@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization["user-name"]
    else:
        g.user = "Anonymous"


@app.route("/api", methods=['POST','DELETE','GET'])
async def my_microservice():
    response = jsonify({"Hello":g.user})
    return response

@app.route('/api/person/<person_id>', methods=['GET'])
async def person(person_id):
    return {'Hello':person_id}

if __name__ == "__main__":
    app.run(port=8000)