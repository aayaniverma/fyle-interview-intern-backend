from flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from core.models import Assignment, db
principal_assignments_resources = Blueprint('principal_bp', __name__)

@principal_assignments_resources.route('/principal/assignments', methods=['GET'])
def list_all_assignments():
    principal = request.headers.get('X-Principal')
    if not principal:
        return jsonify({'error': 'Missing principal header'}), 401
    # Fetch and return assignments
    return jsonify({'data': []})

@principal_assignments_resources.route('/principal/teachers', methods=['GET'])
def list_all_teachers():
    principal = request.headers.get('X-Principal')
    if not principal:
        return jsonify({'error': 'Missing principal header'}), 401
    # Fetch and return teachers
    return jsonify({'data': []})

@principal_assignments_resources.route('/assignments/grade', methods=['POST'])
def grade_assignment():
    data = request.json
    assignment_id = data.get('id')
    grade = data.get('grade')

    assignment = Assignment.query.get(assignment_id)
    if not assignment:
        return jsonify({'error': 'Assignment not found'}), 404

    if assignment.state != 'SUBMITTED':
        return jsonify({'error': 'Assignment must be in SUBMITTED state to be graded'}), 400

    assignment.grade = grade
    db.session.commit()

    return jsonify({'message': 'Assignment graded successfully'}), 200