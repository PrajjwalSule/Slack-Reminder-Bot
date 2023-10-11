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
- Then click to install on workspace.
- Select your workspace where you want to connect that bot, then click on allow.
- After succesfully connected to your workspace you will find the **`OAuth Token`**.
- Copy that Token.
- Paste that Token in notepad or word in your loacl system for a moment.

### Create an channel name as reminders in your slack workspace.
- Create a private channel in your workspace called as **`reminders`**

### Add that app to your workspace and channel.
- Now add your created app to the **`reminders`** channel.

### Paste that token in SLACK_TOKEN variable.
- Get that copies token.
- Paste those credentials on .env file in variable name as **SLACK_TOKEN**
