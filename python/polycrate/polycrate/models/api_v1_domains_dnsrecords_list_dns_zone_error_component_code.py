from typing import Literal

ApiV1DomainsDnsrecordsListDnsZoneErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_DOMAINS_DNSRECORDS_LIST_DNS_ZONE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsListDnsZoneErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_domains_dnsrecords_list_dns_zone_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsListDnsZoneErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_DNS_ZONE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_DNS_ZONE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
