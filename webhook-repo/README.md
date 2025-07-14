# GitHub Webhook Receiver

A Flask-based webhook receiver that captures GitHub events (Push, Pull Request, Merge) and stores them in MongoDB with a real-time UI. This implementation is based on the reference repository structure provided by Techstax.

## Features

- **GitHub Webhook Integration**: Receives webhook events from GitHub repositories
- **MongoDB Storage**: Stores event data with proper schema using Flask-PyMongo
- **Real-time UI**: Beautiful, responsive interface that polls data every 15 seconds
- **Blueprint Architecture**: Clean, modular Flask application structure
- **Event Types Supported**:
  - Push events
  - Pull Request events
  - Merge events (bonus feature)

## Prerequisites

- Python 3.7+
- MongoDB (local or cloud)
- GitHub repository for testing

## Installation

1. Create a virtual environment:

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start MongoDB (if using local):

```bash
# On Windows
mongod

# On macOS/Linux
sudo systemctl start mongod
```

## Usage

1. Start the Flask application:

```bash
python run.py
```

2. The application will be available at `http://localhost:5000`

3. Set up GitHub webhook:
   - Go to your GitHub repository settings
   - Navigate to Webhooks
   - Add webhook with URL: `http://your-domain.com/webhook/receiver`
   - Select events: Push, Pull Request, Pull Request Review
   - Set content type to `application/json`

## API Endpoints

- `GET /` - Main UI page
- `POST /webhook/receiver` - GitHub webhook endpoint
- `GET /api/events` - Get all events from MongoDB

## Project Structure

```
webhook-repo/
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── extensions.py        # MongoDB configuration
│   ├── webhook/
│   │   ├── __init__.py      # Webhook blueprint
│   │   └── routes.py        # Webhook endpoints
│   ├── ui/
│   │   ├── __init__.py      # UI blueprint
│   │   └── routes.py        # UI endpoints
│   └── templates/
│       └── index.html       # Real-time UI
└── README.md                # This file
```

## MongoDB Schema

Events are stored with the following structure:

```json
{
  "type": "PUSH|PULL_REQUEST|MERGE",
  "author": "username",
  "to_branch": "branch_name",
  "from_branch": "branch_name", // for PR and Merge events
  "timestamp": "ISO timestamp",
  "formatted_time": "Human readable time",
  "message": "Formatted event message",
  "created_at": "ISO timestamp"
}
```

## UI Features

- **Real-time Updates**: Polls MongoDB every 15 seconds
- **Event Type Indicators**: Color-coded badges for different event types
- **Responsive Design**: Works on desktop and mobile
- **Live Status**: Shows connection status and last update time
- **Smooth Animations**: CSS animations for better UX

## Deployment

### Local Development

```bash
python run.py
```

### Production (using Gunicorn)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Using ngrok for Testing

```bash
# Install ngrok
ngrok http 5000
# Use the ngrok URL as your webhook endpoint
```

## Testing

1. Make changes to your GitHub repository
2. Create pull requests
3. Merge pull requests
4. Check the UI at `http://localhost:5000` to see events

## Troubleshooting

- **MongoDB Connection**: Ensure MongoDB is running and accessible
- **Webhook Delivery**: Check GitHub webhook delivery logs for errors
- **CORS Issues**: The app includes CORS headers for cross-origin requests
- **Port Conflicts**: Change the port in `run.py` if 5000 is in use

## Customizations Made

This implementation extends the base reference repository with:

1. **Complete webhook processing** for Push, Pull Request, and Merge events
2. **MongoDB integration** using Flask-PyMongo
3. **Real-time UI** with 15-second polling
4. **Event formatting** according to requirements
5. **Blueprint architecture** for clean code organization
6. **Error handling** and logging
7. **Responsive design** with modern UI

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License
