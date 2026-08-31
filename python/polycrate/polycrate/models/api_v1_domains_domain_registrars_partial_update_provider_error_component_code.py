from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domain_registrars_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
