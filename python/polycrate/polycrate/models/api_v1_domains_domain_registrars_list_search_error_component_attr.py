from typing import Literal

ApiV1DomainsDomainRegistrarsListSearchErrorComponentAttr = Literal["search"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_domains_domain_registrars_list_search_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListSearchErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
