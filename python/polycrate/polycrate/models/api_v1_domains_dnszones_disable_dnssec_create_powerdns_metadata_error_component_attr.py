from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponentAttr = Literal["powerdns_metadata"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponentAttr
] = {
    "powerdns_metadata",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_powerdns_metadata_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
