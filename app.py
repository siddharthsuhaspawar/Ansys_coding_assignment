# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:12:03 2024

@author: ALW
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json_data = db.Column(JSON)


with app.app_context():
    db.create_all()
        
@app.route('/data', methods=['POST'])
def create_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    new_data = Data(json_data=data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"id": new_data.id}), 201

@app.route('/data/<int:id>', methods=['GET'])
def get_data(id):
    data = Data.query.get_or_404(id)
    return jsonify(data.json_data), 200

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    data = Data.query.get_or_404(id)
    new_data = request.get_json()
    if not new_data:
        return jsonify({"error": "Invalid JSON"}), 400
    data.json_data = new_data
    db.session.commit()
    return jsonify({"message": "Data updated"}), 200

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    data = Data.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({"message": "Data deleted"}), 200



if __name__ == '__main__':
    app.run(debug=True)
    
    


