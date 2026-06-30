# Core Prompt Engineering Principles

**Module 2 — AI-Assisted Development for Development Teams**

<!-- end_slide -->

## Opening scenario

A developer on your team asks AI:

> "Write some code for our API"

The output is generic boilerplate — a Hello World controller, nothing close to what they needed.

**Type in chat: what's the single most important thing missing from that prompt?**


<!-- end_slide -->

## The three Cs

Every developer prompt that works has three things.

**Clarity** — what do you want the model to do?
Task: generate, explain, refactor, test, debug

**Context** — what does the model need to know?
Stack, version, existing code, file, constraints

**Constraints** — what are the rules?
Style, patterns, things to avoid

<!-- pause -->

That prompt had none of them. Let's look at each one.

<!-- end_slide -->

## Clarity: task and format

Vague:
> "Write a controller"

<!-- pause -->

Clear:
> "Generate a FastAPI GET endpoint that returns a list of users as `list[UserResponse]`"

<!-- pause -->

The task is the verb. The format is what the output should look like.
If you can't state both in one sentence, the prompt isn't ready.

<!-- end_slide -->

## Context: stack, file, state

No context:
> "Generate a controller"

<!-- pause -->

With context:
> "I'm working in a Python 3.11 FastAPI project using SQLAlchemy 2.0 and constructor injection throughout. Add a new router for the Users resource. UserService is already wired in dependencies."

<!-- pause -->

Context tells the model what world it's operating in. Without it, it guesses — and it guesses the average of everything it's ever seen, which is rarely what you need.

<!-- end_slide -->

## Constraints: style, patterns, don'ts

No constraints:
> "Generate a FastAPI router"

<!-- pause -->

With constraints:
> "Use constructor injection via `Depends` — not global state. Return `list[UserResponse]` with explicit Pydantic models. No bare `dict` return types. Follow the pattern in the existing `products` router."

<!-- pause -->

Constraints are how you encode your team's standards. The model doesn't know your codebase — you have to tell it what good looks like.

<!-- end_slide -->

## Discussion — type in chat

Look at these two prompts. Both are asking for the same thing.

**Prompt A:**
> "Explain what `@router.get` does"

**Prompt B:**
> "I'm new to FastAPI. Explain what Pydantic response models do — specifically what they change about validation and OpenAPI schema compared to returning a dict. Give a concrete example."

**Which produces more useful output for a developer joining a new team — and why?**


<!-- end_slide -->

## Zero-shot, few-shot, chain-of-thought

These aren't techniques to memorise — they're descriptions of what you're already doing.

**Zero-shot**: just ask. Works for well-known patterns and quick lookups.
> "Explain what a Pydantic `BaseModel` response type does in FastAPI"

<!-- pause -->

**Few-shot**: give an example, ask for another. Works when style or format matters.
> "We write services like this: [example]. Generate a similar one for `OrderService`."

<!-- pause -->

**Chain-of-thought**: ask for reasoning before the answer. Works for complex tasks where accuracy matters.
> "First explain what this method does, then identify any issues, then show a refactored version."

<!-- end_slide -->

## When to use which

| Technique | Use when |
|---|---|
| Zero-shot | Well-known patterns, quick answers |
| Few-shot | You want specific style or format |
| Chain-of-thought | Complex refactoring, debugging, design decisions |

<!-- pause -->

**The practical rule:** start zero-shot. If the output doesn't match your needs, add an example (few-shot) or ask for reasoning first (chain-of-thought). Don't reach for complexity before you need it.

<!-- end_slide -->

## Iterative refinement

The first output is rarely the right output. That's not a failure — it's the process.

**Read the output as a diagnosis:**
- Wrong version or API? → Missing context
- Wrong style or patterns? → Missing constraints or a few-shot example
- Plausible but subtly incorrect? → Add chain-of-thought; ask it to reason before answering

<!-- pause -->

**Demo:** *(Run a vague prompt live — "Refactor this code" with no context — show the output, then diagnose it together. Ask the group: what would you add?)*

<!-- end_slide -->

## Refinement in practice

Starting prompt:
> "Refactor this code"

<!-- pause -->

After one round:
> "Refactor this Python method to use a list comprehension instead of a for loop. Keep the return type as `list[str]`."

<!-- pause -->

After another:
> "Refactor this Python method to use a list comprehension instead of a for loop. Keep the return type as `list[str]`. Filter out `None` entries rather than raising. Here's the method: [code]"

<!-- pause -->

Each round adds one thing. You don't need to write the perfect prompt first time — you need to read the output and know what to add.

<!-- end_slide -->

## Summary

1. **Clarity**: state the task and the output format
2. **Context**: give the model the world it's operating in
3. **Constraints**: encode your standards — style, patterns, don'ts
4. **Techniques**: zero-shot first, add examples or reasoning when needed
5. **Iteration**: read the output as a diagnosis, not a verdict

<!-- end_slide -->

## Calibration: who's using what?

**Show of hands** (30 seconds): Copilot daily? Tried but inconsistent? Mostly sceptical?

Pitch hands-on pace accordingly. Experienced users — contribute examples in breakouts.

<!-- end_slide -->

## The three Cs and Jira tickets

**For BAs:** A well-structured Jira ticket is a well-structured prompt.

- **Context** — system, stack, current behaviour
- **Clarity** — expected outcome, acceptance criteria
- **Constraints** — validation, errors, out of scope

You'll see this connection live in Module 3's Jira-to-code demo.

<!-- end_slide -->

## Bridge to Module 3

**We've established:**
- How to write prompts that work (3Cs)
- How to recover when they don't (iteration)

**Module 3**: AI-assisted development in Python (and beyond) — generation, explanation, refactoring, testing, and the Jira-to-code moment.

The 3Cs apply to every prompt in Module 3. If the output isn't right, you now know how to fix it.

<!-- end_slide -->

# Questions?

*Module 2 — Core Prompt Engineering Principles*