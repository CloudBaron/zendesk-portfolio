# Web Widget & Ticket Deflection Setup

## Goal
Reduce inbound ticket volume by surfacing Help Center articles before a customer submits a ticket.

---

## Web Widget Configuration

**Location in Zendesk:** Admin Center → Channels → Web Widget (Classic) or Messaging

### Settings Applied

| Setting | Value |
|---------|-------|
| Widget type | Web Widget (Classic) |
| Initial screen | Help Center search |
| Show contact options | Only after search |
| Article suggestions | Enabled (auto-suggest based on search input) |
| "Contact Us" button | Shown only if customer clicks "Still need help?" |

---

## Deflection Flow

```
Customer clicks Help Widget
        ↓
Search bar appears ("How can we help?")
        ↓
Customer types their issue
        ↓
Widget suggests 3–5 matching articles
        ↓
    ┌───────────────────────────────┐
    │ Did the article help?         │
    │  YES → Customer self-serves   │
    │  NO  → "Still need help?"    │
    └───────────────────────────────┘
              ↓ (if No)
        Ticket submission form appears
```

---

## Why This Matters

Ticket deflection is one of the most important KPIs in support operations. Even a 10–15% deflection rate saves significant agent hours per week. Building this into the widget from the start means customers get faster answers and agents spend time on issues that actually need human attention.
