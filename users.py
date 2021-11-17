from settings import *

# Initializing our database
db = SQLAlchemy(app)

class MyEnum(str, enum.Enum):
    active = '1'
    banned = '2'
    pending = '3'

class User(db.Model):
    __tablename__ = 'users'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(), nullable=False)
    last_login = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.Enum(MyEnum))

    def json(self):
        return {'id': self.id, 'name': self.name,
                'email': self.email, 'phone': self.phone, 'password': self.password, 'created_at': self.created_at, 'last_login':                        self.last_login, 'status': self.status}
            # this method we are defining will convert our output to json
        
    def add_user(_name, _email, _phone, _password, _created_at, _last_login, _status):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Movie constructor
        new_user = User(name=_name, email=_email, phone=_phone, password=_password, created_at=_created_at, last_login=_last_login, status=_status)
        db.session.add(new_user)
        db.session.commit()
        
    def get_all_users():
        '''function to get all movies in our database'''
        return [User.json(user) for user in User.query.all()]
    
    def get_user(_id):
        '''function to get movie using the id of the movie as parameter'''
        return [User.json(User.query.filter_by(id=_id).first())]
    
    def update_user(_id, _name, _email, _phone, _password, _created_at, _last_login, _status):
        '''function to update the details of a movie using the id, title,
        year and genre as parameters'''
        user_to_update = User.query.filter_by(id=_id).first()
        user_to_update.name = _name
        user_to_update.email = _email
        user_to_update.phone = _phone
        user_to_update.password = _password
        user_to_update.created_at = _created_at
        user_to_update.last_login = _last_login
        user_to_update.status = _status
        db.session.commit()
        
    def delete_user(_id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        User.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database