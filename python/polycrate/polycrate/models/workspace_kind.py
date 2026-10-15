from typing import Literal

WorkspaceKind = Literal["generic", "polycrate"]

WORKSPACE_KIND_VALUES: set[WorkspaceKind] = {
    "generic",
    "polycrate",
}


def check_workspace_kind(value: str) -> WorkspaceKind:
    if value in WORKSPACE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_KIND_VALUES!r}")
