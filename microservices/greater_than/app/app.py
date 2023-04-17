from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource

class Greater_than(Resource): 
	def get(self, a, b):
		return {'res': int(a) > int(b)}

app = Flask(__name__)
api = Api(app)
api.add_resource(Greater_than, '/<a>/<b>')

if __name__ =="__main__":
	app.run(debug=True, port=5059, host="0.0.0.0")