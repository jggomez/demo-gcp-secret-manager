from typing import Final
from google.cloud import secretmanager
from dotenv import load_dotenv

load_dotenv()

SECRET_USER_ID: Final = "user"
SECRET_PASSWORD_ID: Final = "password"
DECODE_FORMAT: Final = "UTF-8"
PROJECT_ID = "devhack-55d18"


def get_name(project_id, secret_id, version):
    return f"projects/{project_id}/secrets/{secret_id}/versions/{version}"


def get_secret(project_id, secret_id, version="latest"):
    name = get_name(project_id, secret_id, version)
    client = secretmanager.SecretManagerServiceClient()
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode(DECODE_FORMAT)
    return payload


if __name__ == '__main__':
    print(get_secret(PROJECT_ID, SECRET_USER_ID))
    print(get_secret(PROJECT_ID, SECRET_PASSWORD_ID))
    print(get_secret(PROJECT_ID, SECRET_USER_ID, 1))
