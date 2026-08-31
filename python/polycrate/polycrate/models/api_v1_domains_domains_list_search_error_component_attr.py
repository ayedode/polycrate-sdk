from typing import Literal

ApiV1DomainsDomainsListSearchErrorComponentAttr = Literal["search"]

API_V1_DOMAINS_DOMAINS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DomainsDomainsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_domains_domains_list_search_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsListSearchErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
