from flask import Blueprint, request, jsonify
from .utils import validate_email

contact_blueprint = Blueprint('contact', __name__)

@contact_blueprint.route('/contact', methods=['POST'])
def handle_contact():
    """Handles POST requests to the '/api/contact' endpoint."""
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        message = data['message']
        company = data.get('company', None)  # Optional field
        
        # Validate required fields
        if not name or not email or not message:
            raise ValueError('Name, email, and message fields are required')

        # Validate email format
        if not validate_email(email):
            raise ValueError('Invalid email format')

        # if not name or not email or not text:
        #     raise ValueError('Name, email, and text fields are required')

        return jsonify({'success': True})

    except (KeyError, ValueError) as e:
        return jsonify({'success': False, 'error': f'Invalid request data: {e}'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'An error occurred: {e}'}), 500
