from typing import Literal

WorkspaceScope = Literal["system", "user"]

WORKSPACE_SCOPE_VALUES: set[WorkspaceScope] = {
    "system",
    "user",
}


def check_workspace_scope(value: str) -> WorkspaceScope:
    if value in WORKSPACE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_SCOPE_VALUES!r}")
