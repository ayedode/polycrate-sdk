from typing import Literal

ApiV1DomainsDomainsListDnsZoneErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_DOMAINS_DOMAINS_LIST_DNS_ZONE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsListDnsZoneErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_domains_domains_list_dns_zone_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsListDnsZoneErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_LIST_DNS_ZONE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_DNS_ZONE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
