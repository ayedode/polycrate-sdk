from typing import Literal

ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponentAttr = Literal["use_platform_dns"]

API_V1_DOMAINS_DOMAINS_CREATE_USE_PLATFORM_DNS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponentAttr
] = {
    "use_platform_dns",
}


def check_api_v1_domains_domains_create_use_platform_dns_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_USE_PLATFORM_DNS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_USE_PLATFORM_DNS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
