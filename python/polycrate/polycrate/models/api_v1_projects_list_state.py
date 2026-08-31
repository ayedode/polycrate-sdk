from typing import Literal

ApiV1ProjectsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PROJECTS_LIST_STATE_VALUES: set[ApiV1ProjectsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_projects_list_state(value: str) -> ApiV1ProjectsListState:
    if value in API_V1_PROJECTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_STATE_VALUES!r}")
