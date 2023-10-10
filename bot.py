import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import yaml
from datetime import datetime, date
import time

with open("config.yaml", 'r') as file:
    data = yaml.safe_load(file)


env_path = Path('.')/".env"
load_dotenv(dotenv_path=env_path)
CHANEL_NAME = 'reminders'

try:
    SECRET_TOKEN = os.environ['SLACK_TOKEN']
except KeyError:
    SECRET_TOKEN = "Token not available!"

client = slack.WebClient(token=SECRET_TOKEN)


def morningReminder():
    for key, values in data.items():
        if key == "Reminders":
            messages = values['Morning']

    for time in messages.keys():
        if time == datetime.now().strftime("%I:%M"):
            reminder = f"{date.today()} : {datetime.now().strftime('%I:%M %p')} : {messages[time]}"
            client.chat_postMessage(channel=CHANEL_NAME, text=reminder)




def eveningReminders():
    for key, values in data.items():
        if key == "Reminders":
            messages = values['Evening']    

    for time in messages.keys():
        if time == datetime.now().strftime("%I:%M"):
            reminder = f"{date.today()} : {datetime.now().strftime('%I:%M %p')} : {messages[time]}"
            client.chat_postMessage(channel=CHANEL_NAME, text=reminder)



if __name__ == "__main__":
    current_time = datetime.now().strftime("%H")
    # current_time2 = datetime.now().strftime("%I:%M")   
    # print("Current Time =", current_time)
    # print("Current_time2:", current_time2)

    if current_time < '12':
        for i in range(3):
            morningReminder()
            time.sleep(2)

    else:
        for i in range(3):
            eveningReminders()
            time.sleep(2)