from typing import Literal

ApiV1BlockRolloutConfigsListSearchErrorComponentAttr = Literal["search"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_block_rollout_configs_list_search_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsListSearchErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
