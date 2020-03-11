from app import db

class Readings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, index=True)
    time = db.Column(db.Float, index=True)

    def __repr__(self):
        return '<Readings {}>'.format(self.temperature)
