from typing import Literal

ApiV1BlocksListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_BLOCKS_LIST_STATE_NOT_VALUES: set[ApiV1BlocksListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_blocks_list_state_not(value: str) -> ApiV1BlocksListStateNot:
    if value in API_V1_BLOCKS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_STATE_NOT_VALUES!r}")
