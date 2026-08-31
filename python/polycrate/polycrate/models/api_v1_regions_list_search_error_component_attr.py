from typing import Literal

ApiV1RegionsListSearchErrorComponentAttr = Literal["search"]

API_V1_REGIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_regions_list_search_error_component_attr(value: str) -> ApiV1RegionsListSearchErrorComponentAttr:
    if value in API_V1_REGIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
