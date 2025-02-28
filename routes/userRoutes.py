from flask import Flask, jsonify, request
from flask import Blueprint

user_api = Blueprint('user_api', __name__)

@user_api.route("/usuarios", methods = ['GET'])
def index():
    return "Bienvenido Usuario"