# AI-Assisted Development in Python (and Beyond)

**Module 3 — AI-Assisted Development for Development Teams**

<!-- end_slide -->

## Opening scenario

A developer on your team has just used AI to generate a complete `LoanService` — model, repository, service, and route. It took three minutes.

They're about to paste it into the codebase.

**Type in chat: what do you check before you let that go in?**

<!-- end_slide -->

## Four things AI can do in your workflow
<!-- incremental_lists: true -->
1. **Generate** boilerplate you'd otherwise write by hand
2. **Explain** legacy code or patterns you don't recognise
3. **Refactor** existing code toward a clearer style
4. **Test** by generating pytest or Jest coverage for a method

Each one has a failure mode. Today is about using them well and spotting when the output isn't good enough to use.

<!-- end_slide -->

## Generation: what it's good for

Fast, consistent boilerplate: SQLAlchemy models, DTOs, repository interfaces, service stubs, API routes.

The risk isn't that AI generates the wrong thing. It's that it generates the right pattern for the **wrong version** of your stack.

<!-- pause -->

**Demo:** Generate a Book model without specifying versions — then add "Python 3.11, SQLAlchemy 2.0, constructor injection" and compare.

<!-- end_slide -->

## Generation: build incrementally

Don't ask for everything in one prompt.

Start with the model. Review it. Then add the repository. Review it. Then the service.

<!-- pause -->

Each step is a checkpoint. If the model uses the wrong mapping style, fix it before the repository inherits the mistake across three files.

<!-- pause -->

**The rule of thumb:** the longer the output, the less you'll read it carefully. Keep generation prompts scoped to one layer at a time.

<!-- end_slide -->

## When to generate, when to write

| Generate with AI | Review carefully | Write manually |
|---|---|---|
| Models, DTOs, repository interfaces | Business logic with edge cases | Security and auth logic |
| CRUD operations | Performance-critical paths | Payment and compliance code |
| Service stubs | Complex algorithms | Anything your team will be audited on |

<!-- pause -->

**Discussion:** A `PricingService` with complex discount logic has been stable for two years. A junior asks to use AI for a new discount tier. What do you tell them?

<!-- end_slide -->

## Explanation: the layered approach

Build understanding in layers:
<!-- incremental_lists: true -->
1. **What does it do?** — functional behaviour, input/output
2. **Why was it written this way?** — historical context, patterns of the era
3. **What's the modern equivalent?** — migration path
4. **What breaks if I change it?** — dependencies, callers, assumptions

Layer 4 is the one most people skip — and the one that causes the most incidents.

<!-- end_slide -->

## Explanation: the question that matters most

Layer 4 is what AI is most likely to get wrong without your codebase context.

Use AI for layers 1–3. For layer 4, use AI to generate the *questions to ask*, then answer them by reading the code.

<!-- end_slide -->

## Refactoring: safety first
<!-- incremental_lists: true -->
1. Ask AI to generate tests for the existing code
2. Run them — they should pass
3. Ask AI to refactor
4. Run the tests again — they should still pass
5. Read the diff: does the behaviour match?

If step 2 fails — stop. Don't refactor until you understand why.

<!-- end_slide -->

## Refactoring: what AI is and isn't good at

Good at: mechanical transformations — loops to comprehensions, extracting methods, adding type hints.

Less reliable at: knowing which behaviour is intentional. A check that looks defensive might be load-bearing.

<!-- pause -->

**After every refactor:** "Is there anything that looked wrong but was doing something important?"

<!-- end_slide -->

## Testing: generate, run, refine
<!-- incremental_lists: true -->
1. Generate — specify pytest or Jest, name the scenarios
2. Run — don't assume they pass
3. Diagnose — a failing test is a prompt refinement opportunity
4. Refine — add missing setup or constraints

**The thing not to do:** read tests, think they look right, skip running them.

<!-- end_slide -->

## Testing: what scenarios to ask for
<!-- incremental_lists: true -->
- Happy path with valid input
- `None` input
- Empty string or empty collection
- Whitespace-only string (distinct from empty)
- Repository returns nothing
- Repository throws

**Then add one the model won't think of.**

For `find_book_by_isbn`: does the model test `"   "` separately from `""` when the guard uses `strip()`?

<!-- end_slide -->

## Frontend: same patterns

React, Node, and PHP teams: generation, explanation, refactor, and test follow the same workflow — only syntax changes.

See the worked example handout. The whitespace-only gap case appears in every language.

<!-- end_slide -->

## Jira-to-code: requirements as prompts

**For the whole room — especially BAs.**

A vague ticket → vague prompt → vague code.

A ticket with context, clarity, and constraints → useful first draft + testable acceptance criteria.

<!-- pause -->

**Demo:** Strong Jira ticket pasted into Copilot Chat — watch acceptance criteria become tests.

<!-- end_slide -->

## The evaluation checklist
<!-- incremental_lists: true -->
- Does it run / type-check?
- Right Python / framework versions?
- Team conventions (injection, naming, error shape)?
- Security — validation, SQL, secrets?
- Testable — is there a test, or can one be written?

**Back to the opening scenario.** Which question do you ask first?

<!-- end_slide -->

## Summary

1. **Generate** incrementally — one layer at a time
2. **Explain** in layers — don't skip "what breaks"
3. **Refactor** safely — tests before and after
4. **Test** iteratively — generate, run, refine
5. **Review** before every paste
6. **Tickets** — good Jira stories are good prompts

<!-- end_slide -->

## Bridge to Module 4

Module 4: sidecar vs inline workflows, context headers, and team standards.

The evaluation checklist applies to output from all modes.

<!-- end_slide -->

# Questions?

*Module 3 — AI-Assisted Development in Python (and Beyond)*
