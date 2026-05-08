import os
import requests
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# Load environment variables
# We try loading from the current directory, and also from venv/.env
# just in case the .env file is stored there.
load_dotenv()
load_dotenv("venv/.env")

# Retrieve Notion credentials
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def push_tasks_to_notion(action_items: list):
    """
    Pushes extracted action items to a Notion database.
    
    Database columns expected in Notion:
    - Task (Title property)
    - Owner (Rich text property)
    - Status (Select property)
    """
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("Error: NOTION_TOKEN or NOTION_DATABASE_ID missing in environment.")
        return

    # The Notion API endpoint for creating a new page (which adds a row to a database)
    url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    for item in action_items:
        task_name = item.get("task", "Untitled Task")
        owner_name = item.get("owner", "Unknown")

        # Define the payload for the Notion API
        payload = {
            "parent": {
                "database_id": NOTION_DATABASE_ID
            },
            "properties": {
                # Column: Task (Title)
                "Task": {
                    "title": [
                        {
                            "text": {
                                "content": task_name
                            }
                        }
                    ]
                },
                # Column: Owner (Text/Rich_text)
                "Owner": {
                    "rich_text": [
                        {
                            "text": {
                                "content": owner_name
                            }
                        }
                    ]
                },
                # Column: Status (Select) with default "To Do"
                "Status": {
                    "select": {
                        "name": "To Do"
                    }
                }
            }
        }

        try:
            # Make the POST request to Notion API
            response = requests.post(url, json=payload, headers=headers)
            
            # Print success or error response from Notion
            if response.status_code in [200, 201]:
                print(f"Success: Task '{task_name}' added to Notion.")
            else:
                print(f"Failed to add task '{task_name}'. Status: {response.status_code}")
                print(response.text)
                
        except Exception as e:
            # Catch exceptions to prevent the FastAPI server from crashing
            print(f"Exception while pushing to Notion: {e}")
