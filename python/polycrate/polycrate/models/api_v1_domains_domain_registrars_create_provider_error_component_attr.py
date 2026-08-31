from typing import Literal

ApiV1DomainsDomainRegistrarsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_domains_domain_registrars_create_provider_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateProviderErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
