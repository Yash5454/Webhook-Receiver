# GitHub Webhook System Setup Guide

This guide will help you set up and test the complete GitHub webhook system with MongoDB storage and real-time UI.

## System Overview

The system consists of two repositories:

1. **webhook-repo**: Flask application that receives GitHub webhooks and stores data in MongoDB
2. **action-repo**: GitHub repository that triggers webhook events

## Prerequisites

- Python 3.7+
- MongoDB (local or cloud)
- GitHub account
- ngrok (for local testing)

## Step 1: Set Up MongoDB

### Option A: Local MongoDB

```bash
# Install MongoDB Community Edition
# Windows: Download from https://www.mongodb.com/try/download/community
# macOS: brew install mongodb-community
# Ubuntu: sudo apt install mongodb

# Start MongoDB
mongod
```

### Option B: MongoDB Atlas (Cloud)

1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create a free cluster
3. Get your connection string
4. Update the `.env` file with your connection string

## Step 2: Set Up Webhook Receiver

1. **Clone and set up webhook-repo:**

```bash
cd webhook-repo
pip install -r requirements.txt
```

2. **Configure environment:**

```bash
cp env.example .env
# Edit .env with your MongoDB URI
```

3. **Start the webhook receiver:**

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Step 3: Expose Local Server (for testing)

Since GitHub needs to reach your local server, use ngrok:

```bash
# Install ngrok
# Download from https://ngrok.com/download

# Expose your local server
ngrok http 5000
```

Copy the ngrok URL (e.g., `https://abc123.ngrok.io`)

## Step 4: Create Action Repository

1. **Create a new GitHub repository named `action-repo`**

2. **Clone it locally:**

```bash
git clone https://github.com/yourusername/action-repo.git
cd action-repo
```

3. **Add the sample files from this project:**

```bash
# Copy the src/, tests/ directories and README.md
```

4. **Push to GitHub:**

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

## Step 5: Configure GitHub Webhook

1. **Go to your action-repo on GitHub**
2. **Navigate to Settings → Webhooks**
3. **Click "Add webhook"**
4. **Configure the webhook:**

   - **Payload URL**: `https://your-ngrok-url.ngrok.io/webhook/receiver`
   - **Content type**: `application/json`
   - **Secret**: (leave empty for testing)
   - **Events**: Select "Let me select individual events"
   - **Events to send**:
     - ✅ Push
     - ✅ Pull requests
     - ✅ Pull request reviews

5. **Click "Add webhook"**

## Step 6: Test the System

### Test 1: Push Event

```bash
# In your action-repo
echo "# Updated README" >> README.md
git add .
git commit -m "Update README"
git push origin main
```

**Expected Result**: You should see a push event in the UI:
`"YourUsername" pushed to "main" on [timestamp]`

### Test 2: Pull Request Event

```bash
# Create a new branch
git checkout -b feature-branch

# Make changes
echo "New feature" > feature.txt
git add .
git commit -m "Add new feature"
git push origin feature-branch
```

**On GitHub:**

1. Go to your repository
2. Click "Compare & pull request"
3. Create the pull request

**Expected Result**: You should see a pull request event:
`"YourUsername" submitted a pull request from "feature-branch" to "main" on [timestamp]`

### Test 3: Merge Event

**On GitHub:**

1. In the pull request, click "Merge pull request"
2. Confirm the merge

**Expected Result**: You should see a merge event:
`"YourUsername" merged branch "feature-branch" to "main" on [timestamp]`

## Step 7: Verify UI Updates

1. **Open the webhook receiver UI** at `http://localhost:5000`
2. **Check that events appear** within 15 seconds of the action
3. **Verify the formatting** matches the requirements:
   - Push: `{author} pushed to {to_branch} on {timestamp}`
   - Pull Request: `{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}`
   - Merge: `{author} merged branch {from_branch} to {to_branch} on {timestamp}`

## Troubleshooting

### Webhook Not Receiving Events

1. **Check ngrok is running** and the URL is correct
2. **Verify webhook is active** (green checkmark in GitHub)
3. **Check webhook delivery logs** in GitHub repository settings
4. **Ensure Flask app is running** and accessible

### Events Not Appearing in UI

1. **Check MongoDB connection** in Flask logs
2. **Verify API endpoint** `/api/events` returns data
3. **Check browser console** for JavaScript errors
4. **Ensure polling is working** (check network tab)

### MongoDB Connection Issues

1. **Verify MongoDB is running**
2. **Check connection string** in `.env` file
3. **Test connection** with MongoDB Compass or mongo shell
4. **For Atlas**: Ensure IP whitelist includes your IP

### Common Issues

- **CORS errors**: The app includes CORS headers
- **Port conflicts**: Change port in `app.py` if 5000 is in use
- **ngrok URL changes**: Update webhook URL when ngrok restarts

## Production Deployment

For production, consider:

1. **Deploy to cloud service** (Heroku, AWS, Google Cloud)
2. **Use HTTPS** for webhook URLs
3. **Add webhook secrets** for security
4. **Set up monitoring** and logging
5. **Use MongoDB Atlas** or managed MongoDB service

## Repository Links

After setup, provide these links:

- **webhook-repo**: `https://github.com/yourusername/webhook-repo`
- **action-repo**: `https://github.com/yourusername/action-repo`

## Testing Checklist

- [ ] MongoDB connection working
- [ ] Flask app running on localhost:5000
- [ ] ngrok exposing the webhook endpoint
- [ ] GitHub webhook configured and active
- [ ] Push events being captured
- [ ] Pull request events being captured
- [ ] Merge events being captured
- [ ] UI displaying events correctly
- [ ] UI updating every 15 seconds
- [ ] Event formatting matches requirements

## Support

If you encounter issues:

1. Check the Flask application logs
2. Verify MongoDB connection
3. Test webhook delivery in GitHub
4. Check browser developer tools
5. Ensure all dependencies are installed
