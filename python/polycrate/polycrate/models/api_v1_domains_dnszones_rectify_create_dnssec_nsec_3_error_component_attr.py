from typing import Literal

ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponentAttr = Literal["dnssec_nsec3"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponentAttr
] = {
    "dnssec_nsec3",
}


def check_api_v1_domains_dnszones_rectify_create_dnssec_nsec_3_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
