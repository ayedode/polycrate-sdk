from typing import Literal

ApiV1DomainsDnszonesEnableDnssecCreateNsec3ErrorComponentAttr = Literal["nsec3"]

API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NSEC_3_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesEnableDnssecCreateNsec3ErrorComponentAttr
] = {
    "nsec3",
}


def check_api_v1_domains_dnszones_enable_dnssec_create_nsec_3_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesEnableDnssecCreateNsec3ErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NSEC_3_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NSEC_3_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
