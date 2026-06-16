import json
from os import path
from datetime import datetime

data_file = "data.json"

def load_users():
    if not path.exists(data_file):
        return []
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_users(users):
    with open(data_file, "w") as f:
        json.dump(users, f, indent=4)

def initialize_file():
    if not path.exists(data_file):
        save_users([])

def log_event(event, LANID):
    
    with open("logs.txt", "a") as f:
        f.write(f"{LANID} WAS {event} {datetime.now()}\n")