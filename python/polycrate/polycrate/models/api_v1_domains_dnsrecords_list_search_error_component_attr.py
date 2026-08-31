from typing import Literal

ApiV1DomainsDnsrecordsListSearchErrorComponentAttr = Literal["search"]

API_V1_DOMAINS_DNSRECORDS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_domains_dnsrecords_list_search_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsListSearchErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
