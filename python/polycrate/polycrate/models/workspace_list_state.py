from typing import Literal

WorkspaceListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

WORKSPACE_LIST_STATE_VALUES: set[WorkspaceListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_workspace_list_state(value: str) -> WorkspaceListState:
    if value in WORKSPACE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_LIST_STATE_VALUES!r}")
