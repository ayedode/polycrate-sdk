from typing import Literal

ApiV1BlockRolloutConfigsListKind = Literal["config", "trigger"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_VALUES: set[ApiV1BlockRolloutConfigsListKind] = {
    "config",
    "trigger",
}


def check_api_v1_block_rollout_configs_list_kind(value: str) -> ApiV1BlockRolloutConfigsListKind:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_VALUES!r}")
