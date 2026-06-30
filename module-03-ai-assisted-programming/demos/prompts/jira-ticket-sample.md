# LIB-284 — Find book by ISBN returns null for whitespace-only input

## Context

Library Management API (Python 3.11, FastAPI, SQLAlchemy 2.0, MySQL).  
`BookService.find_book_by_isbn` exists; QA reports inconsistent behaviour for edge-case ISBN strings.

## User story

**As a** librarian  
**I want** ISBN lookup to treat blank and whitespace-only strings as invalid  
**So that** we never hit the database with meaningless queries

## Acceptance criteria

- [ ] `None` input → returns `None`, repository not called
- [ ] `""` input → returns `None`, repository not called
- [ ] `"   "` (whitespace only) → returns `None`, repository not called
- [ ] Valid ISBN → returns book from repository
- [ ] Unknown ISBN → returns `None` (not an exception)
- [ ] Unit tests cover all cases above with `unittest.mock`

## Technical notes

- Guard clause must use strip-aware check (not only `if not isbn`)
- Follow existing `BookService` constructor injection pattern
- Do not add new dependencies

## Out of scope

- Controller/route changes
- ISBN format validation regex (separate story)
