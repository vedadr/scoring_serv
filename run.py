from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

def model_calc_hearth_risk_1(args):
    print(str(args) + 'this is in model')
    
    return 0.5


parser = reqparse.RequestParser()
parser.add_argument('weight')

class CalcRisk(Resource):
    def get(self, todo_id):
        return todo_id

    def post(self, todo_id):
        args = parser.parse_args()
        print('this is not it' + str(args) + str(todo_id))
        if todo_id == 'calc_hearth_risk':
            print("this is in model")
            return model_calc_hearth_risk_1(args)

api.add_resource(CalcRisk, '/calcrisk/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

#
# TODOS = {
#     'todo1': {'task': 'build an API'},
#     'todo2': {'task': '?????'},
#     'todo3': {'task': 'profit!'},
# }

# parser.add_argument('task')

#
# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))

# Todo
# shows a single todo item and lets you delete a todo item
# class Todo(Resource):
#     def get(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         return TODOS[todo_id]
#
#     def delete(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         del TODOS[todo_id]
#         return '', 204
#
#     def put(self, todo_id):
#         args = parser.parse_args()
#         task = {'task': args['task']}
#         TODOS[todo_id] = task
#         return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
# class TodoList(Resource):
#     def get(self):
#         return TODOS
#
#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task': args['task']}
#         return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
# api.add_resource(TodoList, '/todos')
# api.add_resource(Todo, '/todos/<todo_id>')
