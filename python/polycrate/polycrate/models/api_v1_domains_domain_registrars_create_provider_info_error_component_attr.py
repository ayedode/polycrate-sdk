from typing import Literal

ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponentAttr = Literal["provider_info"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_INFO_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponentAttr
] = {
    "provider_info",
}


def check_api_v1_domains_domain_registrars_create_provider_info_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_INFO_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_INFO_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
