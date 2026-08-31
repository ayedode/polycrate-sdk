from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponentAttr = Literal["dns_zone_id"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponentAttr
] = {
    "dns_zone_id",
}


def check_api_v1_domains_dnsrecords_partial_update_dns_zone_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
