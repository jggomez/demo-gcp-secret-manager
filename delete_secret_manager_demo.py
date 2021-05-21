from typing import Final
from google.cloud import secretmanager
from dotenv import load_dotenv

load_dotenv()

SECRET_ID: Final = "secret1"
DECODE_FORMAT: Final = "UTF-8"
PROJECT_ID = "devhack-55d18"


def delete_secret_value(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_path(project_id, secret_id)
    client.delete_secret(request={"name": name})


if __name__ == '__main__':
    delete_secret_value(PROJECT_ID, SECRET_ID)
