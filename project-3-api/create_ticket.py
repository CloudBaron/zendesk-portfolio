import os
import requests
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
EMAIL = os.getenv("ZENDESK_EMAIL")
API_TOKEN = os.getenv("ZENDESK_API_TOKEN")

# Zendesk API endpoint
url = f"https://{SUBDOMAIN}.zendesk.com/api/v2/tickets.json"

# Ticket data to create
ticket_data = {
    "ticket": {
        "subject": "Auto-generated ticket from API script",
        "comment": {
            "body": "This ticket was created programmatically using the Zendesk REST API. "
                    "This simulates how an external system (like a product alert or CRM) "
                    "could automatically open a support ticket."
        },
        "priority": "normal",
        "tags": ["api-generated", "portfolio-project"]
    }
}

def create_ticket():
    """Create a new ticket in Zendesk via the REST API."""
    response = requests.post(
        url,
        json=ticket_data,
        auth=(f"{EMAIL}/token", API_TOKEN)
    )

    if response.status_code == 201:
        ticket = response.json()["ticket"]
        print(f"✅ Ticket created successfully!")
        print(f"   ID:      #{ticket['id']}")
        print(f"   Subject: {ticket['subject']}")
        print(f"   Status:  {ticket['status']}")
        print(f"   URL:     https://{SUBDOMAIN}.zendesk.com/agent/tickets/{ticket['id']}")
    else:
        print(f"❌ Failed to create ticket.")
        print(f"   Status code: {response.status_code}")
        print(f"   Response: {response.text}")

if __name__ == "__main__":
    create_ticket()
