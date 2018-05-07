from pprint import pprint
import os
import sys
import json


def read_message_file(f: str) -> dict:
    with open(f, encoding="UTF-8") as file:
        messages = json.loads(file.read())
        return messages


def read_data(fbpath: str):
    dirs = os.walk(fbpath + "/messages")
    message_paths = []
    for dir in dirs:
        if "message.json" in dir[2]:
            message_paths.append(dir[0] + "/" + dir[2][0])
    read_message_file(message_paths[0])


if __name__ == '__main__':
    facebook_path = os.environ["FBPATH"]
    read_data(facebook_path)
