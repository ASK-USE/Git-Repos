# /app/models.py

from . import db

class DataModel(db.Model):
    __tablename__ = 'RESTtesttTable2'  # Tabellenname
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String(50), unique=True, nullable=False)
    asset_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    data = db.Column(db.JSON, nullable=True) # *
    last_updated = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())

# * Hinweis: Das JSON-Feld 'data' wurde beibehalten für zusätzliche flexible Daten.