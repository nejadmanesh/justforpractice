# backend/integrations/notion_client.py
import requests, os

def create_notion_page(prompt: str):
    notion_token = os.getenv("NOTION_TOKEN")
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": {"type": "page_id", "page_id": "YOUR_PARENT_PAGE_ID"},
        "properties": {
            "title": [{"text": {"content": f"ایده جدید: {prompt}"}}]
        }
    }
    r = requests.post(url, headers=headers, json=data)
    return {"notion_result": r.json()}
