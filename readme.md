# AI-Assisted Development: Prompt Engineering for Development Teams

**A one-day, in-person course for mixed development teams and business analysts.**

---

## What this course is

This course is for teams who are already aware of AI tools and want a common, well-grounded foundation — not an introduction from scratch. Developers who use GitHub Copilot, Codex, or Claude daily will make their instincts explicit and portable; developers who have tried tools but not yet got consistent value will be properly equipped to start; business analysts will understand enough to engage meaningfully with how requirements flow into AI-assisted development.

The focus is prompt engineering and deliberate AI use in **VS Code** with **Copilot, Codex, and Claude** integrations, applied primarily to a **Python backend** and **React / Node / PHP** frontend stack. Principles apply across any AI surface.

By the end of the day, delegates will have a working mental model for when to use which AI mode, how to write prompts that produce usable output first time, and a starting-point framework for consistent team-level use.

---

## Who it is for

- **Developers** working across Python (backend), React, Node, and PHP (frontend), with MySQL and AWS in the environment
- **Mixed Copilot adoption** — some daily users, some occasional, some sceptical
- **Three business analysts** who want to understand how developers use AI and how Jira tickets become effective prompt context

No prior prompt engineering knowledge is assumed. VS Code with AI integrations installed is expected.

---

## Learning outcomes

By the end of the day, delegates will be able to:

- Explain how large language models work, where they fail, and how to verify their output
- Write prompts that are clear, contextual, and constrained — and diagnose whether poor output is a model or prompt problem
- Use AI for code generation, explanation, refactoring, and test writing in Python (and recognise the same patterns in JS/PHP)
- Choose between inline completion, chat/sidecar, and spec-driven development based on the task
- Draft a context header that steers AI output toward team coding standards
- *(BAs)* Connect well-structured Jira tickets to effective developer prompts

---

## Course structure

### Module 1 — GenAI and the Developer Landscape

Shared foundation: what generative AI is, the LLM landscape (ChatGPT, Copilot, Codex, Claude), public vs enterprise AI, capabilities and limitations, and honest framing for sceptics — AI changes what good work looks like, not whether good work is needed.

### Module 2 — Core Prompt Engineering

The three Cs (clarity, context, constraints), zero-shot vs few-shot, chain-of-thought, iterative refinement, and debugging prompts. Includes a brief calibration on current tool usage. **BA track:** the three Cs map directly to writing better Jira tickets.

### Module 3 — AI-Assisted Development in Python (and Beyond)

Generation, explanation, refactoring, and testing with human review non-negotiable. Hands-on in Python; a worked example for the frontend stack; **cross-functional Jira-to-code demonstration** for developers and BAs.

### Module 4 — Tooling Strategies and Working Standards

Sidecar vs integrated workflows, context headers, working with multiple VS Code integrations, encoding coding standards into prompts, company policy, and a team-level starting-point checklist. Hands-on: draft and test a context header.

---

## Follow-up session

A second session is planned approximately three months after the foundation day — shaped by what the team has encountered in practice (Python deep dives, standardising context headers, agent workflows, review of real team examples).


---
## Each module contains

- `slides.md` — Markdown presenterm-compatible slide deck
- `exercises/README.md` — Delegate-facing exercise instructions
- `demos/` — Facilitator notes and sample prompts (Modules 1–3)

---

## Prerequisites for delegates

- VS Code with GitHub Copilot, Codex, and/or Claude integrations active
- Python 3.11+ for Module 3 hands-on (or use provided teaching examples)
- Frontend developers may use the React/Node/PHP worked example in Module 3 instead of Python for one exercise
