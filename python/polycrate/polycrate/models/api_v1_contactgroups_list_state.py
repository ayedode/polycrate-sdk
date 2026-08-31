from typing import Literal

ApiV1ContactgroupsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CONTACTGROUPS_LIST_STATE_VALUES: set[ApiV1ContactgroupsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_contactgroups_list_state(value: str) -> ApiV1ContactgroupsListState:
    if value in API_V1_CONTACTGROUPS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_STATE_VALUES!r}")
