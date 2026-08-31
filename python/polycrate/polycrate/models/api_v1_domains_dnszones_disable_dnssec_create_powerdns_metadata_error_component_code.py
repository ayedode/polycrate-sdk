from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_powerdns_metadata_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
