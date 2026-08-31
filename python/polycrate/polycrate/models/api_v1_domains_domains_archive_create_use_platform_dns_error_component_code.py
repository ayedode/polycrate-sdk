from typing import Literal

ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_USE_PLATFORM_DNS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_archive_create_use_platform_dns_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_USE_PLATFORM_DNS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_USE_PLATFORM_DNS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
