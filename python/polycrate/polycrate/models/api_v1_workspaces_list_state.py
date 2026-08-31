from typing import Literal

ApiV1WorkspacesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_WORKSPACES_LIST_STATE_VALUES: set[ApiV1WorkspacesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_workspaces_list_state(value: str) -> ApiV1WorkspacesListState:
    if value in API_V1_WORKSPACES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_STATE_VALUES!r}")
