# /app/resources.py

from flask_restful import Resource, reqparse
from flask import current_app
from .models import DataModel
from . import db
from sqlalchemy.exc import SQLAlchemyError

parser = reqparse.RequestParser()
parser.add_argument("client_id", type=str, required=True, help="Client ID cannot be blank!")
parser.add_argument("asset_name", type=str, required=True, help="Asset name cannot be blank!")
parser.add_argument("quantity", type=int, required=True, help="Quantity cannot be blank!")
parser.add_argument("data", type=dict, required=False)  # Optional für zusätzliche JSON-Daten

class DataResource(Resource):
    def get(self):
        try:
            data_entries = DataModel.query.all()
            data = [{
                "client_id": entry.client_id,
                "asset_name": entry.asset_name,
                "quantity": entry.quantity,
                "data": entry.data,
                "last_updated": str(entry.last_updated)  # Convert to string to ensure JSON serialization
            } for entry in data_entries]
            return data, 200
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error: {str(e)}")
            return {"message": "Database error occurred"}, 500
        except Exception as e:
            current_app.logger.error(f"Unexpected error: {str(e)}")
            return {"message": "An unexpected error occurred"}, 500
    
    def post(self):
        try:
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
        except SQLAlchemyError as e:
            db.session.rollback()
            current_app.logger.error(f"Database error: {str(e)}")
            return {"message": "Database error occurred"}, 500
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Unexpected error: {str(e)}")
            return {"message": "An unexpected error occurred"}, 500