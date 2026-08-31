from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_dnssec_nsec_3_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_NSEC_3_ERROR_COMPONENT_CODE_VALUES!r}"
    )
