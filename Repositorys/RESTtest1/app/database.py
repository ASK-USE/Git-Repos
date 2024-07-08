# /app/database.py

from .models import DataModel
from . import db

def add_data(client_id, data):
    new_data = DataModel(client_id=client_id, data=data)
    db.session.add(new_data)
    db.session.commit()
    return {"message": "Data added"}, 201

def get_data():
    data_entries = DataModel.query.all()
    data = [{"client_id": entry.client_id, "data": entry.data} for entry in data_entries]
    return data, 200
