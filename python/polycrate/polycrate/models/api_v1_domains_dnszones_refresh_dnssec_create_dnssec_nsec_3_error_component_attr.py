from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponentAttr = Literal["dnssec_nsec3"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponentAttr
] = {
    "dnssec_nsec3",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_dnssec_nsec_3_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
