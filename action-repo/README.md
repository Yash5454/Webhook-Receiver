# GitHub Action Repository

This repository triggers GitHub webhook events for testing the webhook receiver.

## Setup

1. Create a new GitHub repository named `action-repo`
2. Set up webhook in repository settings:
   - URL: `http://your-webhook-domain.com/webhook`
   - Events: Push, Pull requests, Pull request reviews
3. Clone and make changes to test webhooks

## Testing

- Push commits to trigger push events
- Create pull requests to trigger PR events
- Merge pull requests to trigger merge events
- Check webhook receiver UI for events
