from typing import Literal

ApiV1DomainsDomainsListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DOMAINS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DomainsDomainsListScopeErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_domains_domains_list_scope_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsListScopeErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
