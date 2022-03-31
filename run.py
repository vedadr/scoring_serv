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
