from typing import Literal

ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_domains_domain_registrars_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
