from flask import Blueprint, render_template, jsonify
from app.extensions import mongo

ui = Blueprint('UI', __name__)

@ui.route('/')
def index():
    """Serve the main UI page"""
    return render_template('index.html')

@ui.route('/api/events', methods=['GET'])
def get_events():
    """API endpoint to get all events from MongoDB"""
    try:
        # Get the latest 50 events, sorted by creation time
        events = list(mongo.db.events.find({}, {'_id': 0}).sort('created_at', -1).limit(50))
        
        # Convert datetime objects to strings for JSON serialization
        for event in events:
            if 'created_at' in event:
                event['created_at'] = event['created_at'].isoformat()
        
        return jsonify(events)
        
    except Exception as e:
        print(f"Error fetching events: {str(e)}")
        return jsonify({'error': str(e)}), 500 