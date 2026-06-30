# Module 2 — Exercises

**For delegates.** This exercise runs during the Module 2 lab session. Your facilitator will manage timing and the shared doc.

---

## Objective

By the end of this exercise you will be able to:

- Diagnose what's wrong with a prompt that produces poor output
- Apply the three Cs to produce output that's actually usable
- Recognise zero-shot, few-shot, chain-of-thought, and iterative refinement when you see them
- Give and receive specific, actionable feedback on a real prompt

---

## Format

No breakout rooms today — instead, everyone works from a shared Google Doc your facilitator will link. You'll add your own example to it, then the group reviews entries together.

**Remember:** Use only synthetic or already-shared examples — not proprietary code or internal APIs.

**BAs:** this applies to ticket wording as well as chat prompts — think "acceptance criteria" when you're looking for constraints.

---

## Exercise: Find it in the wild

### Step 1 — Individual mining (5–7 minutes)

Open your actual AI chat history — Copilot Chat sidebar, ChatGPT/Claude web history, Codex, whatever you've used this morning or in recent work. Find:

- One prompt that shows clarity, context, or constraints clearly. Note which one(s).
- One prompt that's an example of zero-shot, few-shot, or chain-of-thought (even if you didn't know the name for it at the time).
- Bonus: a spot where you refined a prompt across two or more turns and the output visibly improved.

No visible history (inline-completion-only, or no AI chat tool)? Pull a recent Jira ticket instead — the same diagnosis applies to ticket wording.

Don't tidy up what you find — paste it as it actually was.

### Step 2 — Post to the shared doc (3–5 minutes)

Add a row to the shared doc with your example:

| Name | Prompt (pasted as-is) | Technique used (zero-shot / few-shot / CoT / refinement) | Strongest C | Weakest or missing C | One-line fix |
|------|------------------------|------------------------------------------------------------|-------------|-----------------------|---------------|

BAs: add your ticket example to the second table instead:

| Name | Ticket text (pasted as-is) | Strongest C | Weakest or missing C | One-line fix |
|------|------------------------------|-------------|-----------------------|---------------|

If you're sat near someone, comparing notes before you post is fine — it just isn't a formal breakout.

### Step 3 — Whole-room walk-through (10 minutes)

Your facilitator scrolls the doc live and picks out a handful of entries to discuss. For each one: which C is present, which is weakest, and would adding the missing one actually change the output?

Watch for the pattern across the room — usually one C gets dropped more often than the others. That's the gap Module 3 picks up when you move from prompts to code.

---

## Extensions

If you finish early or want to go deeper:

1. **Failure modes:** Ask AI the same question three times with slightly different phrasing. How much does the output vary? What does that tell you about how fragile prompt design is?

2. **Constraint stress-test:** Take a prompt that worked well and deliberately remove one constraint. Does the output degrade? Which constraint mattered most?

3. **Template for your team:** Write a prompt template your team could reuse for a common task — refactoring, test generation, or controller/router scaffolding. Focus on the context and constraints that are always true for your codebase, with placeholders for what changes each time.

---

## Before you move to Module 3

Make sure you have:

- [ ] Found and tagged at least one real prompt (or ticket) against the three Cs
- [ ] Identified the technique used (zero-shot / few-shot / chain-of-thought / refinement) in at least one example
- [ ] Reviewed two or three other delegates' entries in the shared doc
- [ ] Noted the most common missing C across the room

In Module 3 you'll apply these techniques to Python development (and see the same patterns for React/Node/PHP). The 3Cs apply to every prompt — and to Jira tickets. If the output isn't right, you now know how to diagnose it.

---

## Alternative version (requires breakout rooms)

If a future delivery has working breakout rooms, the original four-exercise version (diagnose-and-rewrite on planted prompts, a few-shot writing task, a chain-of-thought decision task, and a swap-and-critique round) is kept in `archive-breakout-version.md` in this folder.
