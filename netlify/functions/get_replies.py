import json
import csv
import os

def handler(event, context):
    filename = "replies_log.csv"
    if not os.path.isfile(filename):
        return {
            "statusCode": 200,
            "body": json.dumps({"replies": []})
        }

    replies = []
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            replies.append(row)

    return {
        "statusCode": 200,
        "body": json.dumps({"replies": replies})
    }
