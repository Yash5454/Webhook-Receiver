# GitHub Webhook System - Project Overview

## 🎯 Project Summary

This project implements a complete GitHub webhook system that captures repository events (Push, Pull Request, Merge) and displays them in a real-time UI. The system consists of two repositories working together to demonstrate webhook integration with MongoDB storage.

## 📁 Project Structure

```
Techstax/
├── webhook-repo/                 # Flask webhook receiver
│   ├── app.py                   # Main Flask application
│   ├── requirements.txt         # Python dependencies
│   ├── env.example             # Environment configuration template
│   ├── README.md               # Webhook repo documentation
│   └── templates/
│       └── index.html          # Real-time UI with polling
├── action-repo/                 # GitHub repository for testing
│   ├── README.md               # Action repo documentation
│   ├── src/
│   │   ├── main.py             # Sample Python code
│   │   └── utils.py            # Sample utility functions
│   └── tests/
│       └── test_main.py        # Sample test file
├── SETUP_GUIDE.md              # Complete setup instructions
└── PROJECT_OVERVIEW.md         # This file
```

## 🏗️ Architecture

### System Flow

1. **GitHub Repository** (action-repo) triggers events
2. **GitHub Webhook** sends event data to webhook endpoint
3. **Flask Application** (webhook-repo) receives and processes events
4. **MongoDB** stores event data with proper schema
5. **Real-time UI** polls MongoDB every 15 seconds and displays events

### Components

#### 1. Webhook Receiver (webhook-repo)

- **Technology**: Flask, PyMongo, Flask-CORS
- **Features**:
  - GitHub webhook endpoint (`/webhook`)
  - MongoDB integration
  - Event processing for Push, PR, and Merge events
  - REST API endpoint (`/api/events`)
  - Real-time UI with 15-second polling

#### 2. Action Repository (action-repo)

- **Purpose**: Trigger GitHub webhook events
- **Contents**: Sample code files for testing
- **Events**: Push, Pull Request, Merge

#### 3. Real-time UI

- **Technology**: HTML5, CSS3, JavaScript (ES6+)
- **Features**:
  - Modern, responsive design
  - Color-coded event types
  - Live status indicators
  - Smooth animations
  - Mobile-friendly layout

## 📊 MongoDB Schema

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

## 🎨 UI Features

### Event Display Format

- **Push**: `"{author}" pushed to "{to_branch}" on {timestamp}`
- **Pull Request**: `"{author}" submitted a pull request from "{from_branch}" to "{to_branch}" on {timestamp}`
- **Merge**: `"{author}" merged branch "{from_branch}" to "{to_branch}" on {timestamp}`

### Visual Design

- **Modern gradient backgrounds**
- **Card-based event display**
- **Color-coded event types**:
  - 🟢 Green: Push events
  - 🟡 Yellow: Pull Request events
  - 🔴 Red: Merge events
- **Responsive design** for mobile and desktop
- **Smooth animations** and hover effects
- **Live status indicators**

## 🔧 Technical Implementation

### Webhook Processing

```python
# Event type detection
if event_type == 'push':
    process_push_event(payload)
elif event_type == 'pull_request':
    action = payload.get('action')
    if action == 'closed' and payload.get('pull_request', {}).get('merged', False):
        process_merge_event(payload)
    else:
        process_pull_request_event(payload)
```

### Real-time Polling

```javascript
// Poll MongoDB every 15 seconds
setInterval(() => {
  this.loadEvents();
}, 15000);
```

### Event Formatting

```python
# Human-readable timestamp formatting
formatted_time = dt.strftime("%d{0} %B %Y - %I:%M %p UTC".format(
    "th" if 11 <= dt.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(dt.day % 10, "th")
))
```

## 🚀 Key Features

### ✅ Implemented Requirements

- [x] GitHub webhook integration
- [x] MongoDB storage with proper schema
- [x] Real-time UI with 15-second polling
- [x] Push event handling and display
- [x] Pull Request event handling and display
- [x] Merge event handling and display (bonus)
- [x] Clean, minimal UI design
- [x] Proper event formatting as specified

### 🎯 Additional Features

- [x] Responsive design for mobile devices
- [x] Error handling and user feedback
- [x] CORS support for cross-origin requests
- [x] Environment-based configuration
- [x] Comprehensive documentation
- [x] Setup and testing guides

## 📋 Setup Requirements

### Prerequisites

- Python 3.7+
- MongoDB (local or cloud)
- GitHub account
- ngrok (for local testing)

### Dependencies

```
Flask==2.3.3
pymongo==4.5.0
python-dotenv==1.0.0
flask-cors==4.0.0
requests==2.31.0
```

## 🧪 Testing Strategy

### Manual Testing

1. **Push Events**: Make commits and push to repository
2. **Pull Request Events**: Create PRs from feature branches
3. **Merge Events**: Merge pull requests
4. **UI Updates**: Verify events appear within 15 seconds
5. **Format Verification**: Check event messages match requirements

### Automated Testing

- Unit tests for utility functions
- API endpoint testing
- MongoDB connection testing

## 🔒 Security Considerations

### Current Implementation

- CORS headers for cross-origin requests
- Environment-based configuration
- Error handling and logging

### Production Recommendations

- HTTPS for webhook endpoints
- Webhook secret authentication
- Rate limiting
- Input validation
- Secure MongoDB connection

## 📈 Performance Optimizations

### Database

- Indexed queries on `created_at` field
- Limited result sets (50 latest events)
- Efficient MongoDB queries

### UI

- 15-second polling interval (configurable)
- Efficient DOM updates
- Minimal data transfer
- Responsive design

## 🚀 Deployment Options

### Local Development

```bash
python app.py
```

### Production (Gunicorn)

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Cloud Platforms

- **Heroku**: Easy deployment with Procfile
- **AWS**: EC2 or Lambda with API Gateway
- **Google Cloud**: App Engine or Cloud Run
- **Azure**: App Service

## 📚 Documentation

### Included Files

- `SETUP_GUIDE.md`: Complete setup instructions
- `webhook-repo/README.md`: Webhook receiver documentation
- `action-repo/README.md`: Action repository documentation
- `PROJECT_OVERVIEW.md`: This comprehensive overview

### Key Information

- Installation and setup steps
- Testing procedures
- Troubleshooting guide
- Deployment options
- API documentation

## 🎯 Learning Outcomes

This project demonstrates:

- **Webhook Integration**: GitHub webhook setup and processing
- **Database Design**: MongoDB schema design and queries
- **Real-time UI**: JavaScript polling and dynamic updates
- **API Development**: RESTful API design with Flask
- **Event Processing**: Handling different event types
- **Error Handling**: Robust error management
- **Documentation**: Comprehensive project documentation

## 🔮 Future Enhancements

### Potential Improvements

- WebSocket support for real-time updates
- Event filtering and search
- User authentication
- Event analytics and metrics
- Email notifications
- Slack/Discord integration
- Event replay functionality

### Scalability Considerations

- Database sharding for large datasets
- Caching layer (Redis)
- Load balancing for multiple instances
- Event streaming (Kafka/RabbitMQ)
- Microservices architecture

## 📞 Support

For questions or issues:

1. Check the `SETUP_GUIDE.md` for troubleshooting
2. Review Flask application logs
3. Verify MongoDB connection
4. Test webhook delivery in GitHub
5. Check browser developer tools

---

**Project Status**: ✅ Complete and Ready for Testing

This implementation provides a solid foundation for GitHub webhook integration with real-time UI updates, demonstrating modern web development practices and API integration skills.
