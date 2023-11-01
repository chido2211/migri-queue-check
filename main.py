#!/usr/bin/env python3

import requests
migri_bot_endpoint = 'https://networkmigri.boost.ai/api/chat/v2'
diary_nr_1 = ''
output_dir = ''

session = requests.post(
    url=migri_bot_endpoint,
    headers={"Content-Type": "application/json"},
    json={
        "command":"START",
        "filter_values":["enterfinland.fi","english_start_language"],
        "language":"en-US"
    }
)
session_id = session.json()["conversation"]["id"]
action_links = [r["payload"]["links"] for r in session.json()["response"]["elements"] if r["type"] == "links"][0]
check_queue_action_id = [a["id"] for a in action_links if a["text"] == 'My place in queue' or a["text"] == 'Minun jonopaikkani'][0]

requests.post(
    url=migri_bot_endpoint,
    headers={"Content-Type": "application/json"},
    json={
        "client_timezone": "Europe/Helsinki",
        "command": "POST",
        "conversation_id": session_id,
        "filter_values": ["enterfinland.fi", "english_start_language"],
        "id": check_queue_action_id,
        "type": "action_link"
    }
)
_ = requests.post(
    url=migri_bot_endpoint,
    headers={"Content-Type": "application/json"},
    json={
        "client_timezone": "Europe/Helsinki",
        "command": "POST",
        "conversation_id": session_id,
        "filter_values": ["enterfinland.fi", "english_start_language"],
        "type": "text",
        "value": diary_nr_1
    }
)
diary_nr_1_place = [r["payload"]["json"]["data"]["counterValue"] for r in _.json()["response"]["elements"] if r["type"] == "json"][0]
diary_nr_1_place = diary_nr_1_place.replace(',','')


import datetime

x = datetime.datetime.now()

diary_nr_1_str = x.strftime('%d/%m/%Y') + "," + diary_nr_1_place + "\n"

with open(f"{output_dir}/migri_queue_diary1.csv", "a") as f:
    f.write(diary_nr_1_str)

print(f"Diary 1 queue place: {diary_nr_1_place}")
