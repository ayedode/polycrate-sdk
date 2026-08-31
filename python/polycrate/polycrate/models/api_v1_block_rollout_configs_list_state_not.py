from typing import Literal

ApiV1BlockRolloutConfigsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_NOT_VALUES: set[ApiV1BlockRolloutConfigsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_block_rollout_configs_list_state_not(value: str) -> ApiV1BlockRolloutConfigsListStateNot:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_NOT_VALUES!r}"
    )
