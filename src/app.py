from flask import Flask, jsonify, request


app = Flask(__name__)


some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [{ "label": "My first task", "done": False },
    { "label": "My second task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    #json_text = jsonify(todos)
    return todos


@app.route('/todos', methods=['POST'])
def add_new_todo():
    data = request.json
    todos.append(data)
    print("Incoming request with the following body", data)
    print('todos',todos)
    return jsonify(todos)

@app.route('/todos/<int:position>',methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete", position)
    del todos[position]
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
