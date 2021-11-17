import argparse
from employees import *

@app.route('/emps', methods=['GET'])
def get_emps():
    '''Function to get all the users in the database'''
    return jsonify({'Emps': Emp.get_all_emps()})

# route to get user by id
@app.route('/emps/<int:id>', methods=['GET'])
def get_emp_by_id(id):
    return_value = Emp.get_user(id)
    return jsonify(return_value)

# route to add new user
@app.route('/emps', methods=['POST'])
def add_emp():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    request_data["dob"] = datetime.strptime(request_data["dob"], '%d/%m/%y')
    request_data["joining_date"] = datetime.strptime(request_data["joining_date"], '%d/%m/%y %H:%M:%S')
#     password = request_data["password"].encode("utf-8")
#     request_data["password"] = base64.b64encode(password)
    Emp.add_emp(request_data["fname"], request_data["lname"],
                    request_data["eid"], request_data["desig"], request_data["dept"], request_data["photo"],request_data["emailOf"], request_data["emailPr"], request_data["phoneOf"], request_data["phonePr"], request_data["emergency_phone"], request_data["joining_date"], request_data["dob"], request_data["gender"])
    response = Response("Emp added", status = 201, mimetype='application/json')
    return response

# route to update user with PUT method
@app.route('/emps/<int:id>', methods=['PUT'])
def update_emp(id):
    '''Function to edit user in our database using movie id'''
    request_data = request.get_json()
    request_data["dob"] = datetime.strptime(request_data["dob"], '%d/%m/%y')
    request_data["joining_date"] = datetime.strptime(request_data["joining_date"], '%d/%m/%y %H:%M:%S')
    Emp.update_emp(id, request_data["fname"], request_data["lname"],
                    request_data["eid"], request_data["desig"], request_data["dept"], request_data["photo"],request_data["emailOf"], request_data["emailPr"], request_data["phoneOf"], request_data["phonePr"], request_data["emergency_phone"], request_data["joining_date"], request_data["dob"], request_data["gender"])
    response = Response("Emp Updated", status=200, mimetype='application/json')
    return response

# route to delete movie using the DELETE method
@app.route('/users/<int:id>', methods=['DELETE'])
def remove_emp(id):
    '''Function to delete movie from our database'''
    Emp.delete_emp(id)
    response = Response("Emp Deleted", status=200, mimetype='application/json')
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