from typing import Literal

WorkspaceSimpleKind = Literal["generic", "polycrate"]

WORKSPACE_SIMPLE_KIND_VALUES: set[WorkspaceSimpleKind] = {
    "generic",
    "polycrate",
}


def check_workspace_simple_kind(value: str) -> WorkspaceSimpleKind:
    if value in WORKSPACE_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_SIMPLE_KIND_VALUES!r}")
