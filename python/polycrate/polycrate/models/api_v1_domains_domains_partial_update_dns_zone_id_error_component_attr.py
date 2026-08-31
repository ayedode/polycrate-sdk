from typing import Literal

ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponentAttr = Literal["dns_zone_id"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponentAttr
] = {
    "dns_zone_id",
}


def check_api_v1_domains_domains_partial_update_dns_zone_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
