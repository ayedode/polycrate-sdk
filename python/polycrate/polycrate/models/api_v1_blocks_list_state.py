from typing import Literal

ApiV1BlocksListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_BLOCKS_LIST_STATE_VALUES: set[ApiV1BlocksListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_blocks_list_state(value: str) -> ApiV1BlocksListState:
    if value in API_V1_BLOCKS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_STATE_VALUES!r}")
