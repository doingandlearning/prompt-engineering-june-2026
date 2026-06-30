# Tooling Strategies and Working Standards

**Module 4 — AI-Assisted Development for Development Teams**

<!-- end_slide -->

## Opening scenario

A developer on your team has been using Copilot for a month. They use it constantly — but always the same way: type something, accept the suggestion, move on.

Their code works. But their prompts are still vague, the output often needs reworking, and they've never used Chat or written a spec.

**Type in chat: what's the one thing you'd tell them to do differently?**

- Pull out repeated/repetitive prompting
- Make a file with constant constraints to adhere to and have it reference that
- Pair programming/apprenticeship learning - watch/work alongside someone who is doing it well
- If they hadn't written a spec - how they know they are understanding the goal?
- Do you understand the requirements?


<!-- end_slide -->

## Three modes, three mental models

| Mode | Where | Mental model |
|---|---|---|
| Inline (integrated) | Editor, as you type | You're driving. AI suggests the next lines. |
| Sidecar / chat | Copilot, Codex, or Claude panel | You're asking a colleague who can see your code. |
| Spec-driven | Chat + PRD or Jira ticket | You're the architect. AI is the implementer. |

<!-- pause -->

Mixing them up is the most common source of frustration. Each one needs different input to work well.

<!-- end_slide -->

## Mode 1: Inline completion

Copilot watches what you're typing and offers completions — a line, a method body, a block.

<!-- incremental_lists: true -->

**Works well for:**
- Boilerplate you know well — entities, DTOs, constructors
- Completing a pattern you've already started
- Quick edits: missing parameter, switch case, null guard
- Staying in flow — no context switch

<!-- pause -->

**Breaks down when:**
- You haven't given it enough signal — a blank file or a vague method name
- You want something non-obvious — it guesses conservatively
- You need to reason about a design decision

<!-- end_slide -->

## Getting more from inline: signal

Copilot reads your method name, parameters, nearby code, and comments. The more signal, the better the suggestion.

**Name with intent:**
```python
# vague
def process(id): ...

# directed
async def validate_and_save_user_profile(user_id: int) -> ValidationResult: ...
```

<!-- pause -->

**Comment first, then signature:**
```python
# Validate email uniqueness before save. Return ValidationResult with field errors.
async def save_user(dto: UserDto) -> ValidationResult:
```

<!-- pause -->

**Start the pattern:** write the first property — Copilot completes the rest.

<!-- end_slide -->

## Accepting suggestions: the habit

`Tab` accepts everything. `Ctrl+→` accepts word by word. `Esc` rejects.

**Use `Ctrl+→` more than `Tab`.** Reading word by word before accepting is the habit that stops subtle bugs getting in.

<!-- pause -->
<!-- incremental_lists: true -->
**What to watch for:**
- Wrong null handling assumptions
- Validation logic that was elsewhere in the file, silently omitted
- Method names or types that are subtly off from your conventions


**The rule:** if you wouldn't have written it that way, question it before accepting.

<!-- end_slide -->

## Mode 2: Sidecar / chat

A conversation with Copilot, Codex, or Claude that has context about your workspace — open files, selected code, project structure.

<!-- incremental_lists: true -->
**Use Chat when you're thinking, not just writing:**
- You need to understand something — `what does this method actually do?`
- You're making a design decision — `should this be a service or a middleware?`
- You're generating something complex — a full controller, a test suite
- You're stuck and want to think through options before committing


**A practical pattern:**
1. Chat to explore the approach
2. Chat to generate the first draft
3. Inline to fill in details as you refine

Chat is not a better search engine. It's where you do the thinking.

<!-- end_slide -->

## Slash commands

| Command | Use it for |
|---|---|
| `/explain` | Understand what selected code does |
| `/fix` | Diagnose and fix a problem in selected code |
| `/tests` | Generate tests for selected code |
| `/doc` | Generate XML doc comments |
| `/new` | Scaffold a new file or class |

<!-- pause -->

**Select the relevant code first, then run the command.** The selection is the context. Running `/fix` on the whole file when only one method is broken gives Copilot too much noise.

<!-- end_slide -->

## Referencing files in Chat

Pull specific files into the conversation with `#`:

```
#file:task_repository.py — generate a SQLAlchemy implementation of this interface.
Use constructor injection. Follow naming in the file.
```

<!-- pause -->

```
#file:task_service.py — this method raises AttributeError on line 47.
What's the likely cause, and how do I fix it?
```

<!-- pause -->

**Discussion — type in chat:** you're using `/fix` on a `delete_task` method that has three problems — a missing `None` check, `datetime.now()` instead of `datetime.now(timezone.utc)`, and a missing ownership check. Does Copilot catch all three, or does it prioritise? Which would you most want it to catch?


<!-- end_slide -->

## Mode 3: PRD-driven development

Writing a structured specification and using it as the prompt for a complete, consistent feature.
<!-- incremental_lists: true -->
**Why the first two modes aren't enough for a full feature:**
- Inline produces one line at a time
- Chat produces one layer at a time
- Without a shared spec, you get inconsistent naming, missing validation, fragmented error patterns


With a spec, every layer — DTO, service, controller, tests — has the same source of truth.

<!-- pause -->

**The spec is also useful after the AI is done.** Use it in code review. Use it to onboard someone to the feature. It's your requirements document.

<!-- end_slide -->

## What a good PRD contains

A PRD for Copilot needs four things:
<!-- pause -->

- **1. Stack and conventions** — version, injection style, patterns to follow
- **2. Shape of the data** — request fields, types, constraints, response shape
- **3. Behaviour as a list** — what it does step by step, including error cases
- **4. Acceptance criteria** — specific, testable statements Copilot can generate tests against


The acceptance criteria are the most important part. They're what the tests verify. If they're vague, the tests will be vague.

<!-- end_slide -->

## PRD format: plain markdown spec

```markdown
## Feature: Update task priority

**Stack:** Python 3.11, FastAPI, SQLAlchemy 2.0. Constructor injection throughout.

**Endpoint:** PATCH /api/tasks/{id}/priority

**Request:** priority (string — low, medium, high)

**Behaviour:**
- Validate priority is one of the allowed values
- Check the task belongs to the requesting user (OwnerId)
- Update and save
- Return 200 with updated task on success
- Return 404 if task not found
- Return 403 if task belongs to a different user
- Return 400 if priority value is invalid

**Acceptance criteria:**
- [ ] Invalid priority returns 400 with a descriptive error
- [ ] Task not found returns 404
- [ ] Task owned by another user returns 403, not 404
- [ ] Successful update returns 200 with the updated TaskDto
```

<!-- end_slide -->

## PRD format: user story

```markdown
## User Story: Update task priority

**As a** project member
**I want to** change the priority of a task I own
**So that** I can reflect changing urgency without reassigning the task

**Acceptance criteria:**
- [ ] PATCH /api/tasks/{id}/priority accepts Low, Medium, or High
- [ ] Returns 403 if the task belongs to another user — not 404
- [ ] Returns 400 with field-level error if priority value is invalid
- [ ] Returns 200 with updated TaskDto on success

**Technical notes:**
- Stack: Python 3.11, FastAPI, SQLAlchemy 2.0
- Follow existing HTTPException JSON error shape
- See task_repository.py for the repository interface
```

<!-- pause -->

Both formats work. The user story format is easier to share with non-technical stakeholders. The markdown spec format is easier for Copilot to generate consistent output from.

<!-- end_slide -->

## Generating from a spec: the sequence

Paste the spec once. Then generate each layer in sequence, referencing the previous output.

**Step 1 — DTO and validation:**
```
Using this spec: [paste]
Generate UpdateTaskPriorityRequest with validation.
```

**Step 2 — Service method:**
```
Using the spec and the DTO we just created, generate the service method.
Include the ownership check and the error cases from the spec.
```

**Step 3 — Controller endpoint:**
```
Generate the controller endpoint. Follow the response shapes and status codes in the spec.
```

**Step 4 — Tests:**
```
Generate unit tests covering every acceptance criterion in the spec.
```

<!-- end_slide -->

## When output diverges from the spec

It will. The question is how to recover without starting again.

**Naming inconsistency** — the service uses `TaskPriority` but the DTO uses `Priority`:
> "The spec uses `Priority` throughout. Rename `TaskPriority` in the service to match."

<!-- pause -->

**Missing behaviour** — the 403/404 distinction is collapsed into a single 404:
> "The spec requires 403 when the task exists but belongs to another user. Add that check before the 404."

<!-- pause -->

**Wrong error shape** — validation errors don't match team JSON:
> "Error responses should use our FastAPI HTTPException shape. Rewrite error returns to match."

<!-- pause -->

**The principle:** treat divergence as a spec refinement task, not a prompt failure. Add the missing constraint to the spec so the next layer inherits it.

<!-- end_slide -->

## Iterating on the spec itself

If the output keeps diverging in the same way, the spec is missing a constraint.

**Common gaps:**

- Error response shape not specified → add a `**Response format:**` section
- Naming conventions not specified → add `Follow the naming in #file:tasks_router.py`
- Which layer owns which responsibility not specified → add to the behaviour list explicitly

<!-- pause -->

A spec that produces consistent output across all four layers on the first attempt is a well-written spec. Most take one or two iterations to get there. That's normal — and the refined spec is worth keeping.

<!-- end_slide -->

## Choosing your mode

| Task | Mode |
|---|---|
| Writing a DTO or entity | Inline |
| Completing a method you've started | Inline |
| Understanding what legacy code does | Chat `/explain` |
| Diagnosing a bug | Chat `/fix` |
| Generating a full service class | Chat |
| Generating tests for a class | Chat `/tests` |
| Building a feature across multiple files | PRD-driven |
| Onboarding someone to a feature | PRD (spec as documentation) |

<!-- pause -->

**The underlying principle:** AI works best when it has constraints. Inline needs signal. Chat needs a well-framed question with the right files in scope. PRD-driven needs a spec that defines the shape before you ask for it.

<!-- end_slide -->

## Context headers

A short, reusable block you paste (or pin) at the start of chat sessions:

- Stack and versions
- Patterns and folder conventions
- Naming and style rules
- Explicit **do not** list
- Review expectations

**Hands-on:** Draft a header for your codebase area; test it on one generation task; refine one line.

Works alongside PRD/spec work — the spec defines the feature; the header defines the house rules.

<!-- end_slide -->

## Team starting-point checklist

Not a mandate — a basis for deciding what good looks like together:

- When is inline enough vs chat required?
- Where do specs live (Jira, markdown in repo)?
- Who owns context headers per service/team?
- Review before paste — non-negotiable for what categories?
- Enterprise AI only for what data classes?

<!-- end_slide -->

## Summary

1. **Inline** — signal through names, comments, started patterns
2. **Chat** — thinking, slash commands, `#file` / @ references
3. **Spec-driven** — Jira or PRD first; layers in sequence; divergence = spec gap
4. **Context headers** — team standards baked into every session
5. **Shared vocabulary** — so advocates and sceptics can discuss the same workflow

<!-- end_slide -->

# Questions?

*Module 4 — Tooling Strategies and Working Standards*