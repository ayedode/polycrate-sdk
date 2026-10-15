from typing import Literal

WorkspaceTemplateListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

WORKSPACE_TEMPLATE_LIST_STATE_VALUES: set[WorkspaceTemplateListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_workspace_template_list_state(value: str) -> WorkspaceTemplateListState:
    if value in WORKSPACE_TEMPLATE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_TEMPLATE_LIST_STATE_VALUES!r}")
