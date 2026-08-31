from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponentAttr = Literal["dnssec_nsec3"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponentAttr
] = {
    "dnssec_nsec3",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_dnssec_nsec_3_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
