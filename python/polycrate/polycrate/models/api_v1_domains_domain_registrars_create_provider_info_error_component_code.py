from typing import Literal

ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_INFO_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domain_registrars_create_provider_info_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_INFO_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_INFO_ERROR_COMPONENT_CODE_VALUES!r}"
    )
