from typing import Literal

ApiV1IpaddressesListSearchErrorComponentAttr = Literal["search"]

API_V1_IPADDRESSES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_ipaddresses_list_search_error_component_attr(
    value: str,
) -> ApiV1IpaddressesListSearchErrorComponentAttr:
    if value in API_V1_IPADDRESSES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
