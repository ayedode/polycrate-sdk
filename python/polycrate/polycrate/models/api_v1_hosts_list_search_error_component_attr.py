from typing import Literal

ApiV1HostsListSearchErrorComponentAttr = Literal["search"]

API_V1_HOSTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_hosts_list_search_error_component_attr(value: str) -> ApiV1HostsListSearchErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
