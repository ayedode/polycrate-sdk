from typing import Literal

ApiV1BlockRolloutConfigsListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsListKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollout_configs_list_kind_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsListKindErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
