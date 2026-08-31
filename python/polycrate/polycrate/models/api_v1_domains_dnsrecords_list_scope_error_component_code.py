from typing import Literal

ApiV1DomainsDnsrecordsListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_dnsrecords_list_scope_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsListScopeErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
