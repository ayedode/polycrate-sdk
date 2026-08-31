from typing import Literal

ApiV1BlockRolloutConfigsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_VALUES: set[ApiV1BlockRolloutConfigsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_block_rollout_configs_list_state(value: str) -> ApiV1BlockRolloutConfigsListState:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_VALUES!r}")
