from typing import Literal

ApiV1DomainsDnsrecordsListDnsZoneErrorComponentAttr = Literal["dns_zone"]

API_V1_DOMAINS_DNSRECORDS_LIST_DNS_ZONE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsListDnsZoneErrorComponentAttr
] = {
    "dns_zone",
}


def check_api_v1_domains_dnsrecords_list_dns_zone_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsListDnsZoneErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_DNS_ZONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_DNS_ZONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
