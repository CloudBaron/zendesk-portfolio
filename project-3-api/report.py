import os
import csv
import requests
from datetime import datetime, timedelta
from collections import Counter
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
EMAIL = os.getenv("ZENDESK_EMAIL")
API_TOKEN = os.getenv("ZENDESK_API_TOKEN")

# Date range: last 7 days
seven_days_ago = (datetime.utcnow() - timedelta(days=7)).strftime("%Y-%m-%d")

# Zendesk incremental ticket export (search by date)
url = f"https://{SUBDOMAIN}.zendesk.com/api/v2/search.json"
params = {
    "query": f"type:ticket created>{seven_days_ago}",
    "sort_by": "created_at",
    "sort_order": "desc"
}

def fetch_tickets():
    """Fetch all tickets from the last 7 days using the Zendesk search API."""
    tickets = []
    next_url = url

    while next_url:
        response = requests.get(
            next_url,
            params=params if next_url == url else None,
            auth=(f"{EMAIL}/token", API_TOKEN)
        )

        if response.status_code != 200:
            print(f"❌ Error fetching tickets: {response.status_code}")
            print(response.text)
            return []

        data = response.json()
        tickets.extend(data.get("results", []))
        next_url = data.get("next_page")  # Handle pagination

    return tickets

def generate_report(tickets):
    """Count tickets by status and write a CSV report."""
    status_counts = Counter(ticket["status"] for ticket in tickets)

    output_file = "ticket_report.csv"
    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["status", "count"])
        for status, count in sorted(status_counts.items()):
            writer.writerow([status, count])

    print(f"✅ Report generated: {output_file}")
    print(f"   Total tickets (last 7 days): {len(tickets)}")
    print(f"\n   Breakdown by status:")
    for status, count in sorted(status_counts.items()):
        print(f"   {status:<10} {count}")

if __name__ == "__main__":
    print(f"🔍 Fetching tickets created after {seven_days_ago}...")
    tickets = fetch_tickets()

    if tickets:
        generate_report(tickets)
    else:
        print("No tickets found in the last 7 days.")
