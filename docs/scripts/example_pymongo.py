
from flask import Flask, render_template, request, Response
from flask_pymongo import PyMongo
import json
from werkzeug.security import generate_password_hash, check_password_hash #Cifrar y descifrar contraseñas de usuario
from bson import json_util
from bson.objectid import ObjectId

app= Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/minerva'

mongo = PyMongo(app)

@app.route('/models', methods=['POST'])
def create_data():
    model_name = request.json['model_name']
    model = request.json['model']

    if model_name and model:
        id = mongo.db.models.insert(
            {'model_name': model_name, 'model': model}
        )
        response = {
            'id' : str(id),
            'model_name' : model_name,
            'model' : model
        }
        return response
    else:
        return message

@app.route('/models', methods=['GET'])
def get_models():
    models = mongo.db.models.find()
    response = json_util.dumps(models)
    return Response(response, mimetype="application/json")

@app.route('/models/<id>', methods = ['GET'])
def get_model(id):
    model = mongo.db.models.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(model)
    return Response(response, mimetype="application/json")


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    return message



if __name__ == "__main__":
    app.run(debug=True)
