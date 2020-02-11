from flask_restplus import Resource
from ..service.solution_service import get_solution
from ..util.dto import SolutionDto

api = SolutionDto.api


@api.route('/<solution_id>')
@api.param('solution_id', 'The Solution identifier')
@api.response(404, 'Solution not found.')
class Solution(Resource):
    @api.doc('get a solution')
    #@api.marshal_with(_solution)
    def get(self, solution_id):
        """get a solution given its identifier"""
        solution = get_solution(solution_id)
        if not solution:
            api.abort(404)
        else:
            return solution
