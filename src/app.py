from flask import Flask, jsonify, request


app = Flask(__name__)


some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [{ "label": "My first task", "done": False },
    { "label": "My second task", "done": False }]


@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    response_body = {}
    if request.method == 'GET':
        # Devuelve todas las instancias de la colección
        #json_text = jsonify(todos)
        response_body['message'] = 'Listado de todos'
        response_body['results'] = todos
        return response_body,200
    elif request.method == 'POST':
        # Crea o agrega una instacia de la colección
        data = request.json
        todos.append(data)
        response_body['results'] = todos
        print("Incoming request with the following body", data)
        print('todos',todos)
        return response_body


# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     data = request.json
#     todos.append(data)
#     print("Incoming request with the following body", data)
#     print('todos',todos)
#     return jsonify(todos)


@app.route('/todos/<int:position>',methods=['GET','PUT','DELETE'])
def handle_todo(position):
    response_body = {}
    if position >= len(todos):
        response_body['message'] = 'Tarea no existe...'
        response_body['results'] = {}
        return response_body, 404
    if request.method == 'GET':
        response_body['message'] = f'Datos de la tarea {position}'
        response_body['results'] = todos[position]
        return response_body, 200
    if request.method == 'PUT':
        todos[position] = request.json
        response_body['message'] = f'Tarea {position} modificada'
        response_body['results'] = todos[position]
        return response_body, 200
    if request.method == 'DELETE':
        print("This is the position to delete", position)
        del todos[position]
        response_body['message'] = 'Se elimino...'
        response_body['results'] = todos
        return response_body, 200



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
