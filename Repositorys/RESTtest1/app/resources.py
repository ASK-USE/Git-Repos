# /app/resources.py

from flask_restful import Resource, reqparse
from .models import DataModel
from . import db

parser = reqparse.RequestParser()
parser.add_argument("client_id", type=str, required=True, help="Client ID cannot be blank!")
parser.add_argument("asset_name", type=str, required=True, help="Asset name cannot be blank!")
parser.add_argument("quantity", type=int, required=True, help="Quantity cannot be blank!")
parser.add_argument("data", type=dict, required=False)  # Optional für zusätzliche JSON-Daten

class DataResource(Resource):
    def get(self):
        data_entries = DataModel.query.all()
        data = [{
            "client_id": entry.client_id,
            "asset_name": entry.asset_name,
            "quantity": entry.quantity,
            "data": entry.data,
            "last_updated": entry.last_updated
        } for entry in data_entries]
        return data, 200
    
    def post(self):
        args = parser.parse_args()
        existing_entry = DataModel.query.filter_by(client_id=args["client_id"]).first()
        
        if existing_entry:
            existing_entry.asset_name = args["asset_name"]
            existing_entry.quantity = args["quantity"]
            existing_entry.data = args.get("data")
        else:
            new_entry = DataModel(
                client_id=args["client_id"],
                asset_name=args["asset_name"],
                quantity=args["quantity"],
                data=args.get("data")
            )
            db.session.add(new_entry)
        
        db.session.commit()
        return {"message": "Data updated successfully"}, 200
