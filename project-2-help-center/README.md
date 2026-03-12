# Project 2 — Self-Service Knowledge Base

**Difficulty:** Intermediate  
**Time to complete:** 3–4 hours  
**Platform:** Zendesk Guide (Free Trial)

---

## Overview

In this project I built a branded self-service Help Center for NovaTech Support using Zendesk Guide. The goal is ticket deflection — helping customers find answers on their own before submitting a ticket, which reduces agent workload and improves customer satisfaction.

---

## What I Built

- ✅ Branded Help Center (logo, colors, custom homepage text)
- ✅ 2 Article Categories with sections
- ✅ 6 Knowledge Base articles
- ✅ Web Widget configured to suggest articles before ticket submission
- ✅ Ticket deflection flow documented

---

## Help Center Structure

```
NovaTech Help Center
├── Getting Started
│   ├── How to Create Your Account
│   ├── Setting Up Your First Project
│   └── Understanding Your Dashboard
└── Billing & Account
    ├── How to Update Your Payment Method
    ├── Understanding Your Invoice
    └── How to Cancel or Downgrade Your Plan
```

See the [`articles/`](./articles/) folder for the full content of each article.

---

## Ticket Deflection Setup

The Zendesk Web Widget is configured to:
1. Show a search bar as the first screen
2. Suggest relevant Help Center articles based on what the customer types
3. Only show the "Submit a Ticket" option after the customer dismisses the suggestions

This reduces unnecessary tickets by surfacing answers customers could find themselves.

See [`deflection-setup.md`](./deflection-setup.md) for full configuration details.

---

## Screenshots

> Add your screenshots below after completing setup.

```
![Help Center Homepage](./screenshots/help-center-home.png)
![Article Category View](./screenshots/category-view.png)
![Web Widget Deflection](./screenshots/widget-deflection.png)
![Article Example](./screenshots/article-example.png)
```

---

## Skills Demonstrated

- Zendesk Guide setup and branding
- Knowledge base architecture and article writing
- Ticket deflection strategy
- Web Widget configuration
- Self-service support best practices

---

## Files in This Folder

```
project-2-help-center/
├── README.md
├── deflection-setup.md
├── articles/
│   ├── how-to-create-your-account.md
│   ├── setting-up-your-first-project.md
│   ├── understanding-your-dashboard.md
│   ├── how-to-update-payment-method.md
│   ├── understanding-your-invoice.md
│   └── how-to-cancel-or-downgrade.md
└── screenshots/
    └── (your screenshots here)
```
