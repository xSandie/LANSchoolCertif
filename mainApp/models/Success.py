from mainApp.models.base import Base, db


class Success(Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    portraitUri = db.Column(db.String(50))
    info = db.Column(db.Text)
    userId = db.Column(db.Integer)