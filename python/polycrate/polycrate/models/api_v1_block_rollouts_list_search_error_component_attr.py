from typing import Literal

ApiV1BlockRolloutsListSearchErrorComponentAttr = Literal["search"]

API_V1_BLOCK_ROLLOUTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlockRolloutsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_block_rollouts_list_search_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsListSearchErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
