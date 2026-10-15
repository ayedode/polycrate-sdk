from typing import Literal

WorkspaceTemplateState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

WORKSPACE_TEMPLATE_STATE_VALUES: set[WorkspaceTemplateState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_workspace_template_state(value: str) -> WorkspaceTemplateState:
    if value in WORKSPACE_TEMPLATE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_TEMPLATE_STATE_VALUES!r}")
