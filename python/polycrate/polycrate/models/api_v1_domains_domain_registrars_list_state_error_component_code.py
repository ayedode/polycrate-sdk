from typing import Literal

ApiV1DomainsDomainRegistrarsListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_domain_registrars_list_state_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListStateErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
