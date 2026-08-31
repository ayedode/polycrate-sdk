from typing import Literal

ApiV1DomainsDomainRegistrarsListScopeErrorComponentAttr = Literal["scope"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_domains_domain_registrars_list_scope_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListScopeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
