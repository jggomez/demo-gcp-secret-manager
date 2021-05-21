from typing import Final
from google.cloud import secretmanager
from dotenv import load_dotenv
import json

load_dotenv()

SECRET_ID: Final = "secret1"
DECODE_FORMAT: Final = "UTF-8"
PROJECT_ID = "devhack-55d18"


def create_secret(project_id, secret_id):
    parent = f"projects/{project_id}"
    client = secretmanager.SecretManagerServiceClient()
    client.create_secret(
        request={
            "parent": parent,
            "secret_id": secret_id,
            "secret": {"replication": {"automatic": {}}},
        }
    )


def add_secret_value(project_id, secret_id, payload):
    client = secretmanager.SecretManagerServiceClient()
    parent = client.secret_path(project_id, secret_id)
    payload = payload.encode("UTF-8")
    response = client.add_secret_version(
        request={"parent": parent, "payload": {"data": payload}}
    )
    print("Added secret version: {}".format(response.name))


if __name__ == '__main__':
    create_secret(PROJECT_ID, SECRET_ID)
    add_secret_value(PROJECT_ID, SECRET_ID, json.dumps({
                     "name": "Juan", "lastname": "Gomez"}))
