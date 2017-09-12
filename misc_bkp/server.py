from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    #pass
    while (True):
    	continue

from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource

from database import DB

app = Flask(__name__)
app.config.from_envvar('ENV_CONFIG_FILE')

mongo_host = app.config['MONGO_HOST']
mongo_port = app.config['MONGO_PORT']

mongo_endpoint = mongo_host + ":" + str(mongo_port)

db = DB()

@app.route("/<table_type>/<id>", methods=["GET"])
def get_course(table_type, id):
	data = db.readPost(table_type, id)
	if data is None:
		return jsonify({'error': 'Course not found'}), 404
	#print(str(data['_id']))
	return jsonify(data), 200


@app.route("/<table_type>/<id>", methods=["POST"])
def insert_data(table_type, id):
	if not request.json:
		abort(404)
	json_data = request.json
	

	resp = db.insertPost(table_type, id, json_data)
	if resp == False:
		return jsonify({'status': 'failure'}), 404

	return jsonify({'status': 'success'}), 200


@app.route("/<table_type>/<id>", methods=["PUT"])
def update_data(table_type, id):
	if not request.json:
		abort(400)

	resp = db.update(table_type, id, request.json)

	if not resp:
		return jsonify({'error': 'Record not found'}), 404

	return jsonify({'status': 'success'}), 200

@app.route("/<table_type>/<id>", methods=["DELETE"])
def delete_record(table_type, id):
	db.deletePost(table_type, id)

	return jsonify({'status': 'success'}), 200


if __name__ == "__main__":
	app.run(port=app.config['CONFIG_APPLICATION_PORT'])