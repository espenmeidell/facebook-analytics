from pprint import pprint
import os
import sys
import json
from typing import List, Tuple


def create_message_pairs(thread_dict: dict) -> List[Tuple]:
    messages = thread_dict["messages"]
    messages.reverse()
    messages = list(filter(lambda m: "content" in m, messages))
    pairs = []
    for i in range(0, len(messages) - 1):
        pairs.append((messages[i]["content"], messages[i + 1]["content"]))
    return pairs


def read_message_file(f: str) -> dict:
    with open(f, encoding="UTF-8") as file:
        messages = json.loads(file.read())
        return messages


def get_message_paths() -> List[str]:
    dirs = os.walk(os.environ["FBPATH"] + "/messages")
    message_paths = []
    for dir in dirs:
        if "message.json" in dir[2]:
            message_paths.append(dir[0] + "/" + dir[2][0])
    return message_paths


def create_all_message_pairs():
    paths = get_message_paths()
    pairs = []
    for path in paths:
        pairs.extend(create_message_pairs(read_message_file(path)))
    with open(os.environ["FBOUT"] + "/message_pairs.csv", "w") as f:
        for pair in pairs:
            out = '"' + pair[0] + '"' + ", " + '"' + pair[1] + '"' + "\n"
            f.write(out)

    print("Done")

if __name__ == '__main__':
    create_all_message_pairs()
