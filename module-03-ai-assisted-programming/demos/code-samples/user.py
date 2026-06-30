"""Sample User model for Demo 3 refactoring — synthetic example only."""

from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str | None
    is_active: bool
