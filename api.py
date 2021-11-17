import argparse
from users import *

@app.route('/users', methods=['GET'])
def get_users():
    '''Function to get all the users in the database'''
    return jsonify({'Users': User.get_all_users()})

# route to get user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return_value = User.get_user(id)
    return jsonify(return_value)

# route to add new user
@app.route('/users', methods=['POST'])
def add_user():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    request_data["created_at"] = datetime.strptime(request_data["created_at"], '%d/%m/%y %H:%M:%S')
    request_data["last_login"] = datetime.strptime(request_data["last_login"], '%d/%m/%y %H:%M:%S')
    haa = request_data["password"].encode()
    hash_object = hashlib.sha1(haa)
    request_data["password"] = str(hash_object.digest())
#     password = request_data["password"].encode("utf-8")
#     request_data["password"] = base64.b64encode(password)
    User.add_user(request_data["name"], request_data["email"],
                    request_data["phone"], request_data["password"], request_data["created_at"], request_data["last_login"],request_data["status"])
    response = Response("User added", status = 201, mimetype='application/json')
    return response

# route to update user with PUT method
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    '''Function to edit user in our database using movie id'''
    request_data = request.get_json()
    request_data["created_at"] = datetime.strptime(request_data["created_at"], '%d/%m/%y %H:%M:%S')
    request_data["last_login"] = datetime.strptime(request_data["last_login"], '%d/%m/%y %H:%M:%S')
    User.update_user(id, request_data["name"], request_data["email"],
                    request_data["phone"], request_data["password"], request_data["created_at"], request_data["last_login"],request_data["status"])
    response = Response("User Updated", status=200, mimetype='application/json')
    return response

# route to delete movie using the DELETE method
@app.route('/users/<int:id>', methods=['DELETE'])
def remove_movie(id):
    '''Function to delete movie from our database'''
    User.delete_user(id)
    response = Response("User Deleted", status=200, mimetype='application/json')
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