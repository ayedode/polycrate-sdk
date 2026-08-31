from typing import Literal

ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponentAttr = Literal["dnssec_nsec3"]

API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponentAttr
] = {
    "dnssec_nsec3",
}


def check_api_v1_domains_dnszones_update_dnssec_nsec_3_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_NSEC_3_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
