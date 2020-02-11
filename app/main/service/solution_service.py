def get_solution(solution_id):
    package = 'app.main.lib.solutions'

    try:
        solution = getattr(__import__(package, fromlist=[solution_id]), solution_id)
        response_object = {
            'status': 'success',
            'problem': solution.PROBLEM,
            'answer': solution.ANSWER
        }
        return response_object, 200

    except AttributeError as e:
        response_object = {
            'status': 'fail',
            'message': 'The requested solution is not present yet'
        }
        return response_object, 404
