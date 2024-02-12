from flask import Flask, jsonify, request
from projetoapi.credenciais import token, server, database

app = Flask(__name__)
token = token
server = server


from projetoapi import routes

