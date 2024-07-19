from core import db
from core.libs import helpers

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, db.Sequence('users_id_seq'), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return f'<User {self.username}>'

    # Class methods for querying users
    @classmethod
    def filter(cls, *criteria):
        db_query = db.session.query(cls)
        return db_query.filter(*criteria)

    @classmethod
    def get_by_id(cls, user_id):
        return cls.filter(cls.id == user_id).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.filter(cls.email == email).first()

    # Instance methods or properties
    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
