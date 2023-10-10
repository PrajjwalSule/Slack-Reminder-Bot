# Slack-Reminder-Bot

This is a slack bot which will give you the reminder as your choice on your time.

## Steps to use this bot

### Clone this repo
- -  **`git clone git@github.com:PrajjwalSule/Slack-Reminder-Bot.git`**

### Make virtual environment:
- - **`python -m venv .venv`** (Windows)
- - **`python3 -m venv .venv`** (Linux)

### Activate that virtual environment:
- - **`source .venv/Scripts/activate`** (Windows)
- - **`source .venv/bin/activate`** (Linux)

### Create a variable file name as .env
- - **`touch .env`**

### Create a variale name as SLACK_TOKEN in that variable file.
- - **SLACK_TOKEN = ""**


### Install all the dependencies.
- - **`pip -r requirements.txt`** (Windows)
- - **`pip3 -r requirements.txt`** (Linux)


### Modify the config.yaml file according to your time and reminders.

### Create an app on slack-api.
- Go to this link
- - `https://api.slack.com/start/quickstart`
- Click on create slack app button.
- Click on create new app.
- Click From Scratch.
- Write app name and select the workspace.
- Go to OAuth & Permissions.
- Scroll down and find Scopes in the OAuth & Permissions.
- Click on Add an AOuth Scope button.
- Select Chat:write.
- 
### Create an channel name as reminders in your slack workspace.
### Add that app to your workspace and channel.
### Copy the token
### Paste that token in SLACK_TOKEN variable.
