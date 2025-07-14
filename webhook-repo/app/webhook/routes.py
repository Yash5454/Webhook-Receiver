from flask import Blueprint, request, jsonify
from app.extensions import mongo
from datetime import datetime, timezone
import json

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    """Handle GitHub webhook events"""
    try:
        # Get the event type from GitHub headers
        event_type = request.headers.get('X-GitHub-Event')
        
        if not event_type:
            return jsonify({'error': 'No event type found'}), 400
        
        payload = request.json
        
        # Process different event types
        if event_type == 'push':
            process_push_event(payload)
        elif event_type == 'pull_request':
            action = payload.get('action')
            if action == 'closed' and payload.get('pull_request', {}).get('merged', False):
                process_merge_event(payload)
            else:
                process_pull_request_event(payload)
        
        return jsonify({'status': 'success'}), 200
        
    except Exception as e:
        print(f"Error processing webhook: {str(e)}")
        return jsonify({'error': str(e)}), 500

def process_push_event(payload):
    """Process push events"""
    try:
        author = payload.get('pusher', {}).get('name', 'Unknown')
        to_branch = payload.get('ref', '').replace('refs/heads/', '')
        timestamp = payload.get('head_commit', {}).get('timestamp')
        
        if timestamp:
            # Convert to datetime object
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            formatted_time = dt.strftime("%d{0} %B %Y - %I:%M %p UTC".format(
                "th" if 11 <= dt.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(dt.day % 10, "th")
            ))
        else:
            now = datetime.now(timezone.utc)
            formatted_time = now.strftime("%d{0} %B %Y - %I:%M %p UTC".format(
                "th" if 11 <= now.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(now.day % 10, "th")
            ))
        
        now = datetime.now(timezone.utc)
        event_data = {
            'type': 'PUSH',
            'author': author,
            'to_branch': to_branch,
            'timestamp': timestamp or now.isoformat(),
            'formatted_time': formatted_time,
            'message': f'"{author}" pushed to "{to_branch}" on {formatted_time}',
            'created_at': now
        }
        
        mongo.db.events.insert_one(event_data)
        print(f"Stored push event: {event_data['message']}")
        
    except Exception as e:
        print(f"Error processing push event: {str(e)}")

def process_pull_request_event(payload):
    """Process pull request events"""
    try:
        action = payload.get('action')
        if action not in ['opened', 'reopened']:
            return
            
        author = payload.get('pull_request', {}).get('user', {}).get('login', 'Unknown')
        from_branch = payload.get('pull_request', {}).get('head', {}).get('ref', 'Unknown')
        to_branch = payload.get('pull_request', {}).get('base', {}).get('ref', 'Unknown')
        timestamp = payload.get('pull_request', {}).get('created_at')
        
        if timestamp:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            formatted_time = dt.strftime("%d{0} %B %Y - %I:%M %p UTC".format(
                "th" if 11 <= dt.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(dt.day % 10, "th")
            ))
        else:
            now = datetime.now(timezone.utc)
            formatted_time = now.strftime("%d{0} %B %Y - %I:%M %p UTC".format(
                "th" if 11 <= now.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(now.day % 10, "th")
            ))
        
        now = datetime.now(timezone.utc)
        event_data = {
            'type': 'PULL_REQUEST',
            'author': author,
            'from_branch': from_branch,
            'to_branch': to_branch,
            'timestamp': timestamp or now.isoformat(),
            'formatted_time': formatted_time,
            'message': f'"{author}" submitted a pull request from "{from_branch}" to "{to_branch}" on {formatted_time}',
            'created_at': now
        }
        
        mongo.db.events.insert_one(event_data)
        print(f"Stored pull request event: {event_data['message']}")
        
    except Exception as e:
        print(f"Error processing pull request event: {str(e)}")

def process_merge_event(payload):
    """Process merge events (when PR is merged)"""
    try:
        pull_request = payload.get('pull_request', {})
        author = pull_request.get('merged_by', {}).get('login', 'Unknown')
        from_branch = pull_request.get('head', {}).get('ref', 'Unknown')
        to_branch = pull_request.get('base', {}).get('ref', 'Unknown')
        timestamp = pull_request.get('merged_at')
        
        if timestamp:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            formatted_time = dt.strftime("%d{0} %B %Y - %I:%M %p UTC".format(
                "th" if 11 <= dt.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(dt.day % 10, "th")
            ))
        else:
            now = datetime.now(timezone.utc)
            formatted_time = now.strftime("%d{0} %B %Y - %I:%M %p UTC".format(
                "th" if 11 <= now.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(now.day % 10, "th")
            ))
        
        now = datetime.now(timezone.utc)
        event_data = {
            'type': 'MERGE',
            'author': author,
            'from_branch': from_branch,
            'to_branch': to_branch,
            'timestamp': timestamp or now.isoformat(),
            'formatted_time': formatted_time,
            'message': f'"{author}" merged branch "{from_branch}" to "{to_branch}" on {formatted_time}',
            'created_at': now
        }
        
        mongo.db.events.insert_one(event_data)
        print(f"Stored merge event: {event_data['message']}")
        
    except Exception as e:
        print(f"Error processing merge event: {str(e)}") 