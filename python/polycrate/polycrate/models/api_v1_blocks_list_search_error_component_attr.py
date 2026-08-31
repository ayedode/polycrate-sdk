from typing import Literal

ApiV1BlocksListSearchErrorComponentAttr = Literal["search"]

API_V1_BLOCKS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_blocks_list_search_error_component_attr(value: str) -> ApiV1BlocksListSearchErrorComponentAttr:
    if value in API_V1_BLOCKS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
