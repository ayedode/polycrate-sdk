from typing import Literal

ApiV1WorkspaceTemplatesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_WORKSPACE_TEMPLATES_LIST_STATE_VALUES: set[ApiV1WorkspaceTemplatesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_workspace_templates_list_state(value: str) -> ApiV1WorkspaceTemplatesListState:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_STATE_VALUES!r}")
