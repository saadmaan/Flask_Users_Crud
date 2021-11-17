from settings import *

# Initializing our database
db = SQLAlchemy(app)

class Dept(db.Model):
    __tablename__ = 'depts'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(100), nullable=False)
    children = relationship("Emp")
    
    def json(self):
        return {'id': self.id, 'name': self.name}
    
    def add_dept(_name):
        # creating an instance of our Movie constructor
        new_dept = Dept(name=_name)
        db.session.add(new_dept)
        db.session.commit()
        
    def get_all_depts():
        '''function to get all movies in our database'''
        return [Dept.json(dept) for dept in Dept.query.all()]
    
    def get_dept(_id):
        '''function to get movie using the id of the movie as parameter'''
        return [Dept.json(Dept.query.filter_by(id=_id).first())]
    
    def update_dept(_id, _name):
        user_to_update = Dept.query.filter_by(id=_id).first()
        user_to_update.name = _name
        
    def delete_dept(_id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Dept.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database