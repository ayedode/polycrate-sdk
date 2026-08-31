from typing import Literal

ApiV1DomainsDnszonesListSearchErrorComponentAttr = Literal["search"]

API_V1_DOMAINS_DNSZONES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_domains_dnszones_list_search_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesListSearchErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
