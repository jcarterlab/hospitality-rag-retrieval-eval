import os
from dotenv import load_dotenv
import requests

load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_KEY')
PAGE_ID = "3a69c093-3841-8070-aa49-ca507e0dd735"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

response = requests.get(
    f"https://api.notion.com/v1/blocks/{PAGE_ID}/children",
    headers=headers
)

print(response.json())



