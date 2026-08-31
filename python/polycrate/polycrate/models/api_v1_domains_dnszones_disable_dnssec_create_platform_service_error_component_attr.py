from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
