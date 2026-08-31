from typing import Literal

ApiV1BlockRolloutsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_BLOCK_ROLLOUTS_LIST_STATE_VALUES: set[ApiV1BlockRolloutsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_block_rollouts_list_state(value: str) -> ApiV1BlockRolloutsListState:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_STATE_VALUES!r}")
