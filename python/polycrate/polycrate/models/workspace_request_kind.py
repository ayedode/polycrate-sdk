from typing import Literal

WorkspaceRequestKind = Literal["generic", "polycrate"]

WORKSPACE_REQUEST_KIND_VALUES: set[WorkspaceRequestKind] = {
    "generic",
    "polycrate",
}


def check_workspace_request_kind(value: str) -> WorkspaceRequestKind:
    if value in WORKSPACE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_REQUEST_KIND_VALUES!r}")
