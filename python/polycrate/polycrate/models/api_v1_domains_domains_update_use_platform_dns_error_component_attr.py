from typing import Literal

ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponentAttr = Literal["use_platform_dns"]

API_V1_DOMAINS_DOMAINS_UPDATE_USE_PLATFORM_DNS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponentAttr
] = {
    "use_platform_dns",
}


def check_api_v1_domains_domains_update_use_platform_dns_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateUsePlatformDnsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_USE_PLATFORM_DNS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_USE_PLATFORM_DNS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
