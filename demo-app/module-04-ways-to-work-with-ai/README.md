# Module 4 — Tooling Strategies and Working Standards

## Overview

Move from individual experimentation to a consistent, sustainable approach across the team. Written for **VS Code** with **GitHub Copilot, Codex, and Claude** integrations — primarily **Python / FastAPI** backend and **React / Node / PHP** frontend.

The module covers:

1. **Inline (integrated) completion** — suggestions as you type; deliberate signal control
2. **Sidecar / chat** — exploration, explanation, larger generation; slash commands and file references
3. **Spec-driven development** — structured PRD or Jira-style spec before multi-layer generation
4. **Context headers** — encoding team standards so output conforms from the start

## Audience

- VS Code with Copilot, Codex, and/or Claude
- Python backend + React/Node/PHP frontend
- Mixed experience: daily users, occasional, sceptical
- BAs observe tooling discussion; context headers clarify how requirements feed downstream standards

## Learning Objectives

By the end of this module, delegates will be able to:

- Choose inline vs chat vs spec-driven work for a given task
- Apply inline signal techniques (naming, comment-first, pattern-start)
- Use chat slash commands (`/explain`, `/fix`, `/tests`) on real code
- Reference files in chat (`#file:` or @-mentions per tool)
- Write a spec (markdown or user story) that produces consistent multi-layer output
- Draft a **context header** for their area of the codebase and test it on a generation task

## Module Structure

| File | Description |
|---|---|
| `slides.md` | Reveal.js-compatible slide deck |
| `exercises/README.md` | Five delegate exercises (inline, chat, spec, write spec, context header) |

## Time

Approximately 100 minutes including exercises:

- Lecture and demos: ~70 minutes
- Exercises: ~30 minutes (select three or four depending on time)

## Company policy

Leave space in delivery for the client's current AI policy — how to work confidently within it.

## Team checklist

Close with a starting-point checklist (not a mandate): when to use which mode, review before paste, where specs live, context header ownership.
