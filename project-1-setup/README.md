# Project 1 — Help Desk Setup & Ticket Workflow

**Difficulty:** Beginner  
**Time to complete:** 2–3 hours  
**Platform:** Zendesk Suite (Free Trial)

---

## Overview

In this project I set up a fully functional Zendesk instance for a fictional company called **NovaTech Support**. This covers the foundational admin work every support team needs: branding, ticket forms, automated triggers, macros, and SLA policies.

---

## What I Built

- ✅ Branded Zendesk account (company name, logo, support email)
- ✅ Custom ticket form with fields: Issue Type, Priority, Product Area
- ✅ 4 Macros (canned responses) for common ticket types
- ✅ 3 Triggers for ticket automation
- ✅ SLA Policy with 3 tiers

---

## Macros

Macros are saved responses agents can apply to tickets instantly.

| Macro Name | Use Case |
|------------|----------|
| Welcome & Ticket Received | Sent when a ticket is first opened |
| Request More Information | When agent needs details from the customer |
| Escalation Notice | Notifying customer ticket is being escalated |
| Resolved & Closing | Closing a ticket after resolution |

See the [`macros/`](./macros/) folder for the full text of each macro.

---

## Triggers

Triggers fire automatically based on ticket conditions.

| Trigger Name | Condition | Action |
|--------------|-----------|--------|
| Auto-Reply on New Ticket | Ticket created | Send confirmation email to requester |
| Assign to Support Group | Ticket created + Issue Type = Technical | Assign to Technical Support group |
| Urgent Ticket Alert | Priority = Urgent | Notify group via email immediately |

See [`triggers/triggers.md`](./triggers/triggers.md) for full condition/action breakdowns.

---

## SLA Policy

| Tier | First Reply Time | Next Reply Time | Resolution Time |
|------|-----------------|-----------------|-----------------|
| Urgent | 1 hour | 2 hours | 8 hours |
| Normal | 4 hours | 8 hours | 24 hours |
| Low | 8 hours | 24 hours | 72 hours |

See [`sla-policy.md`](./sla-policy.md) for full rationale.

---

## Screenshots

> Add your screenshots below after completing setup. Use this format:

```
![Account Branding](./screenshots/branding.png)
![Ticket Form](./screenshots/ticket-form.png)
![Trigger Setup](./screenshots/trigger-auto-reply.png)
![SLA Policy](./screenshots/sla-policy.png)
```

---

## Skills Demonstrated

- Zendesk account configuration and branding
- Ticket form customization
- Trigger logic (conditions + actions)
- Macro creation for agent efficiency
- SLA policy design and rationale

---

## Files in This Folder

```
project-1-setup/
├── README.md
├── sla-policy.md
├── macros/
│   ├── welcome-ticket-received.txt
│   ├── request-more-info.txt
│   ├── escalation-notice.txt
│   └── resolved-closing.txt
├── triggers/
│   └── triggers.md
└── screenshots/
    └── (your screenshots here)
```
