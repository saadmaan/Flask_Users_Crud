from settings import *

# Initializing our database
db = SQLAlchemy(app)

class MyEnum(str, enum.Enum):
    male = 'male'
    female = 'female'
    others = 'others'

class Emp(db.Model):
    __tablename__ = 'emps'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    eid = db.Column(db.Integer, nullable=False, unique=True)
    desig = db.Column(db.String(80), nullable=False)
    dept = db.Column(db.Integer, nullable=False,ForeignKey('depts.id'))
    # dept = db.Column(db.String(80), nullable=False)
    photo = db.Column(db.String(120), nullable=False)
    emailOf = db.Column(db.String(120), nullable=False,unique=True)
    emailPr = db.Column(db.String(120), nullable=False, unique=True)
    phoneOf = db.Column(db.String(16), nullable=False, unique=True)
    phonePr = db.Column(db.String(16), nullable=False, unique=True)
    emergency_phone = db.Column(db.String(16), nullable=False,unique=True)
    joining_date = db.Column(db.DateTime(), nullable=False)
    dob = db.Column(db.DateTime(), nullable=False)
    gender = db.Column(db.Enum(MyEnum))

    def json(self):
        return {'id': self.id, 'fname': self.fname, 'lname': self.lname, 'eid': self.eid, 'desig': self.desig, 'dept': self.dept, 'photo': self.photo, 'emailOf': self.emailOf, 'emailPr': self.emailPr, 'phoneOf': self.phoneOf, 'phonePr': self.phonePr, 'emergency_phone': self.emergency_phone, 'joining_date': self.joining_date, 'dob': self.dob, 'gender': self.gender}
            # this method we are defining will convert our output to json
        
    def add_emp(_fname, _lname, _eid, _desig, _dept, _photo, _emailOf, _emailPr, _phoneOf, _phonePr, _emergency_phone, _joining_date, _dob, _gender):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Movie constructor
        new_emp = Emp(fname=_fname, lname=_lname, eid=_eid, desig=_desig, dept=_dept, photo=_photo, emailOf=_emailOf, emailPr=_emailPr, phoneOf=_phoneOf, phonePr=_phonePr, emergency_phone=_emergency_phone, joining_date=_joining_date, dob=_dob, gender=_gender)
        db.session.add(new_emp)
        db.session.commit()
        
    def get_all_emps():
        '''function to get all movies in our database'''
        return [Emp.json(emp) for emp in Emp.query.all()]
    
    def get_emp(_id):
        '''function to get movie using the id of the movie as parameter'''
        return [Emp.json(Emp.query.filter_by(id=_id).first())]
    
    def update_emp(_fname, _lname, _eid, _desig, _dept, _photo, _emailOf, _emailPr, _phoneOf, _phonePr, _emergency_phone, _joining_date, _dob, _gender):
        user_to_update = Emp.query.filter_by(id=_id).first()
        user_to_update.fname = _fname
        user_to_update.lname = _lname
        user_to_update.eid = _eid
        user_to_update.desig = _desig
        user_to_update.dept = _dept
        user_to_update.photo = _photo
        user_to_update.emailOf = _emailOf
        user_to_update.emailPr = _emailPr
        user_to_update.phoneOf = _phoneof
        user_to_update.phonePr = _phonePr
        user_to_update.emergency_phone = _emergency_phone
        user_to_update.joining_date = _joining_date
        user_to_update.dob = _dob
        user_to_update.gender = _gender
        db.session.commit()
        
    def delete_emp(_id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Emp.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database