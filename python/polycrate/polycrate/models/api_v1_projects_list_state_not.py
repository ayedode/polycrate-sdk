from typing import Literal

ApiV1ProjectsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PROJECTS_LIST_STATE_NOT_VALUES: set[ApiV1ProjectsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_projects_list_state_not(value: str) -> ApiV1ProjectsListStateNot:
    if value in API_V1_PROJECTS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_STATE_NOT_VALUES!r}")
