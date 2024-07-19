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
    return 'Response for the POST todo'
    pass

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
