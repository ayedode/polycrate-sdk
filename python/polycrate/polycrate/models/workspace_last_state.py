from typing import Literal

WorkspaceLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

WORKSPACE_LAST_STATE_VALUES: set[WorkspaceLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_workspace_last_state(value: str) -> WorkspaceLastState:
    if value in WORKSPACE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_LAST_STATE_VALUES!r}")
