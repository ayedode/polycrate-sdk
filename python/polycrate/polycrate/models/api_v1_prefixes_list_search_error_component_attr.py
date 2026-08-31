from typing import Literal

ApiV1PrefixesListSearchErrorComponentAttr = Literal["search"]

API_V1_PREFIXES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_prefixes_list_search_error_component_attr(value: str) -> ApiV1PrefixesListSearchErrorComponentAttr:
    if value in API_V1_PREFIXES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
