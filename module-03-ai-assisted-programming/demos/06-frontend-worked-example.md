# Worked example: same patterns in React / Node / PHP

## Goal

Give the frontend team a concise parallel to the Python demos — same workflow, different syntax.

**Time:** 5–10 minutes (facilitator-led or self-paced handout).

---

## Generation (React + TypeScript)

**Weak:** "Make a book component"

**Strong:**

> Create a React 18 functional component `BookCard` in TypeScript. Props: `title`, `author`, `isbn`, optional `publishedYear`. Show title and author; ISBN in monospace. No external UI libraries. Export named component only.

---

## Explanation (legacy PHP)

Paste a verbose PHP function (synthetic). Run the same four layers from Demo 2:
1. What does it do?
2. Why was it written this way?
3. What's the modern equivalent (typed PHP 8 / small service class)?
4. What breaks if I change it?

---

## Refactoring (Node)

Verbose `for` loop filtering active users → ask for `filter` + `map` with **identical behaviour**. Tests first with Jest.

---

## Testing (Jest)

```javascript
// findBooksByAuthor(author) — mock repository
// Ask explicitly for: happy path, null, empty string, whitespace-only author
```

**Teaching moment:** whitespace-only input is the gap case — same lesson as `FindBookByIsbn` in Python.

---

## Review checklist

Unchanged from Python: correctness, versions, style, security, testability.
