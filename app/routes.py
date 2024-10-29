from flask import Blueprint, request, jsonify
import requests
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

        # External API URL for sending email
        send_email_url = 'https://custom-portfolio-website-pi.vercel.app/'

        # Payload to send to the external /api/send-email endpoint
        email_payload = {
            'name': name,
            'email': email,
            'message': message,
            'company': company,
        }
        
        # Call the external API
        response = requests.post(send_email_url, json=email_payload)
        
        # Check if the email sending was successful
        if response.status_code == 200:
            return jsonify({'success': True, 'message': 'Contact and email sent successfully'})
        else:
            # Log or handle failed email sending here if needed
            return jsonify({'success': False, 'error': 'Failed to send email'}), response.status_code
        
        
        # if not name or not email or not text:
        #     raise ValueError('Name, email, and text fields are required')

        # return jsonify({'success': True})

    except (KeyError, ValueError) as e:
        return jsonify({'success': False, 'error': f'Invalid request data: {e}'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'An error occurred: {e}'}), 500
