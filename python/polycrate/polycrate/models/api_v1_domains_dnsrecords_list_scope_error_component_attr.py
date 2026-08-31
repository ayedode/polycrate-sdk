from typing import Literal

ApiV1DomainsDnsrecordsListScopeErrorComponentAttr = Literal["scope"]

API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_domains_dnsrecords_list_scope_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsListScopeErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
