from typing import Literal

WorkspaceListKind = Literal["generic", "polycrate"]

WORKSPACE_LIST_KIND_VALUES: set[WorkspaceListKind] = {
    "generic",
    "polycrate",
}


def check_workspace_list_kind(value: str) -> WorkspaceListKind:
    if value in WORKSPACE_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_LIST_KIND_VALUES!r}")
