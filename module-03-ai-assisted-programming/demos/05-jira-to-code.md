# Demo 5: Jira-to-code — cross-functional (developers + BAs)

## Goal

Show the whole room how a well-structured Jira ticket becomes effective prompt context for a developer using AI — and give BAs a direct line between their work and downstream output.

**When:** After Exercise 1–2 hands-on, before or after the frontend worked example (~10 minutes).

---

## Before the demo

- Prepare one **synthetic** Jira ticket (see sample below) — not a real customer ticket.
- Have VS Code open with Copilot Chat or Claude sidecar.
- Optional: show a weak ticket first for contrast (30 seconds).

---

## Steps

### 1. Show a weak ticket (1 min)

```text
Title: Fix book lookup
Description: Books aren't working. Make it work.
```

**Ask BAs:** "Could you implement from this alone? Could AI?"

**Say:** "Vague tickets produce vague prompts — same failure mode as Module 2."

---

### 2. Show a strong ticket (2 min)

Use `prompts/jira-ticket-sample.md` or the ticket below. Highlight:
- **Context:** system area, stack, existing behaviour
- **Clarity:** expected behaviour, inputs, outputs
- **Constraints:** validation rules, error cases, non-goals

**For BAs:** "This is the three Cs applied to requirements — not extra bureaucracy."

---

### 3. Paste ticket as prompt context (4 min)

**Prompt pattern:**

> I'm implementing the following Jira story in our Python/FastAPI library service. Generate only the service method and unit tests — not the controller yet.
>
> [paste full ticket]

Run generation. Point out:
- AI uses acceptance criteria as test scenarios
- Ownership and edge cases appear when the ticket names them
- What's still missing (only the developer knows callers, DB migrations)

---

### 4. Debrief (3 min)

**Developers:** What would you still verify manually?

**BAs:** What one field in your tickets would you add tomorrow?

**Close:** "Good tickets are good prompts. The evaluation checklist from earlier applies to AI output whether the input came from Jira or chat."

---

## Sample Jira ticket (synthetic)

See `prompts/jira-ticket-sample.md`.

---

## BA track note

BAs do not need to run the demo themselves. Their takeaway: structured tickets reduce rework for developers using AI and make acceptance criteria testable from the start.
