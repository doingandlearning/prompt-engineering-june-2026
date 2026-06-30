"""Sample legacy-style code for Demo 2 — synthetic example only."""


class UserBean:
    def __init__(self) -> None:
        self.first_name: str | None = None
        self.last_name: str | None = None
        self.errors: list[str] = []

    def validate_user(self) -> None:
        self.errors.clear()
        if not self.first_name or not self.first_name.strip():
            self.errors.append("First name is required")
        if not self.last_name or not self.last_name.strip():
            self.errors.append("Last name is required")

    def is_valid(self) -> bool:
        return len(self.errors) == 0
