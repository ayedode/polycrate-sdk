from typing import Literal

ApiV1BlockRolloutConfigsListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsListNameExactErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_block_rollout_configs_list_name_exact_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsListNameExactErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
