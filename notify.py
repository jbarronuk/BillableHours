import requests
import os

NTFY_TOPIC = os.environ["NTFY_TOPIC"]

requests.post(
    "https://ntfy.sh/",
    json={
        "topic": NTFY_TOPIC,
        "title": "Hello!",
        "message": "This is a test notification from GitHub Actions",
        "tags": ["wave"],
        "priority": 3
    },
    headers={"Content-Type": "application/json"}
)

print("Notification sent!")