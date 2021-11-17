import argparse
from depts import *

@app.route('/depts', methods=['GET'])
def get_depts():
    '''Function to get all the users in the database'''
    return jsonify({'Depts': Dept.get_all_depts()})

# route to get user by id
@app.route('/depts/<int:id>', methods=['GET'])
def get_dept_by_id(id):
    return_value = Dept.get_dept(id)
    return jsonify(return_value)

# route to add new user
@app.route('/depts', methods=['POST'])
def add_dept():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    Dept.add_dept(request_data["name"])
    response = Response("Dept added", status = 201, mimetype='application/json')
    return response

# route to update user with PUT method
@app.route('/depts/<int:id>', methods=['PUT'])
def update_dept(id):
    '''Function to edit user in our database using movie id'''
    request_data = request.get_json()
    Dept.update_dept(id, request_data["name"])
    response = Response("Dept Updated", status=200, mimetype='application/json')
    return response

# route to delete movie using the DELETE method
@app.route('/depts/<int:id>', methods=['DELETE'])
def remove_dept(id):
    '''Function to delete movie from our database'''
    Dept.delete_dept(id)
    response = Response("Dept Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", type=str, required=True,
        help="ip address of the device")
    ap.add_argument("-o", "--port", type=int, required=True,
        help="ephemeral port number of the server (1024 to 65535)")
    args = vars(ap.parse_args())
    app.run(host=args["ip"], port=args["port"], debug=True, use_reloader=False)
#     app.run(port=8005, debug=True)