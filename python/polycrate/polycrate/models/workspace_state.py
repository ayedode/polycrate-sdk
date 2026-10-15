from typing import Literal

WorkspaceState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

WORKSPACE_STATE_VALUES: set[WorkspaceState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_workspace_state(value: str) -> WorkspaceState:
    if value in WORKSPACE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_STATE_VALUES!r}")
