import json
import boto3
from datetime import datetime

BUCKET_NAME = "semillero-llmbedrock-lrm"

s3 = boto3.client(
    "s3",
    region_name="us-east-1"
)

def new_chat_id():
    return datetime.now().strftime("chat_%Y%m%d_%H%M%S")

def save_chat(messages, filename):
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"{filename}.json",
        Body=json.dumps(
            messages,
            ensure_ascii=False,
            indent=2
        ),
        ContentType="application/json"
    )

def load_chat(filename):
    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=f"{filename}.json"
    )

    content = response["Body"].read().decode("utf-8")
    return json.loads(content)


def get_saved_chats():
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME
    )

    if "Contents" not in response:
        return []

    return sorted(
        (
            obj["Key"][:-5]
            for obj in response["Contents"]
            if obj["Key"].endswith(".json")
        ),
        reverse=True
    )

def delete_chat(filename):
    s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=f"{filename}.json"
    )

def get_chat_title(chat_id):
    messages = load_chat(chat_id)

    for message in messages:
        if message["role"] == "user":
            return message["content"][:40]

    return "Nueva conversación"