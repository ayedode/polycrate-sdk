from typing import Literal

ApiV1PopsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_POPS_LIST_STATE_VALUES: set[ApiV1PopsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pops_list_state(value: str) -> ApiV1PopsListState:
    if value in API_V1_POPS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_STATE_VALUES!r}")
