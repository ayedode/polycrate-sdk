from typing import Literal

ApiV1LoadbalancersRegionsListSearchErrorComponentAttr = Literal["search"]

API_V1_LOADBALANCERS_REGIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_loadbalancers_regions_list_search_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsListSearchErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
