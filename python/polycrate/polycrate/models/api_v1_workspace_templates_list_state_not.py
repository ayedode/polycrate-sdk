from typing import Literal

ApiV1WorkspaceTemplatesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_WORKSPACE_TEMPLATES_LIST_STATE_NOT_VALUES: set[ApiV1WorkspaceTemplatesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_workspace_templates_list_state_not(value: str) -> ApiV1WorkspaceTemplatesListStateNot:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_STATE_NOT_VALUES!r}")
