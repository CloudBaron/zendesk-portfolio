# Triggers — NovaTech Support

Triggers run automatically when a ticket meets a set of conditions. Below are the three triggers configured for this project.

---

## Trigger 1: Auto-Reply on New Ticket

**Purpose:** Let the customer know their ticket was received and give them a reference number.

**Conditions:**
- Ticket is Created

**Actions:**
- Send email to Requester
- Email subject: `We received your request — Ticket #{{ticket.id}}`
- Email body:
  > Hi {{ticket.requester.first_name}},
  > Thanks for reaching out to NovaTech Support. We've received your request and a member of our team will be in touch shortly.
  > Your ticket number is **#{{ticket.id}}**.
  > NovaTech Support Team

---

## Trigger 2: Assign to Technical Support Group

**Purpose:** Route technical issues directly to the right team automatically.

**Conditions:**
- Ticket is Created
- Issue Type (custom field) = Technical

**Actions:**
- Assign to Group: Technical Support
- Set Priority: Normal (if not already set)

---

## Trigger 3: Urgent Ticket Alert

**Purpose:** Immediately notify the support group when a high-priority ticket comes in so it doesn't sit unnoticed.

**Conditions:**
- Ticket is Created OR Ticket Priority changed to Urgent

**Actions:**
- Notify Group: All Support Agents (email)
- Email subject: `🚨 Urgent Ticket Requires Immediate Attention — #{{ticket.id}}`
- Set ticket status: Open
