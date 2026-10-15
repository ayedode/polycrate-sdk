from typing import Literal

WorkspaceRequestScope = Literal["system", "user"]

WORKSPACE_REQUEST_SCOPE_VALUES: set[WorkspaceRequestScope] = {
    "system",
    "user",
}


def check_workspace_request_scope(value: str) -> WorkspaceRequestScope:
    if value in WORKSPACE_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_REQUEST_SCOPE_VALUES!r}")
