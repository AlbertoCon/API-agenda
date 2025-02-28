from flask import Flask, jsonify, request
from flask import Blueprint

contact_api = Blueprint('contact_api', __name__)

@contact_api.route("/contactos", methods = ['GET'])
def index():
    return "Bienvenido a los contactos"
