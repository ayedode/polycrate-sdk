from typing import Literal

ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domain_registrars_list_updated_at_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
