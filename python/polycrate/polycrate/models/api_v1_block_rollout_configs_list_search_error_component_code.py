from typing import Literal

ApiV1BlockRolloutConfigsListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_block_rollout_configs_list_search_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsListSearchErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
