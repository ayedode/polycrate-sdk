from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_domains_dnsrecords_partial_update_dns_zone_id_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateDnsZoneIdErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_DNS_ZONE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
