from typing import Literal

ApiV1DomainsDomainsUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_DOMAINS_DOMAINS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_domains_domains_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
