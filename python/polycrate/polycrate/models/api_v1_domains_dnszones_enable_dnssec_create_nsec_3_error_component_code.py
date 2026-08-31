from typing import Literal

ApiV1DomainsDnszonesEnableDnssecCreateNsec3ErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NSEC_3_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesEnableDnssecCreateNsec3ErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_enable_dnssec_create_nsec_3_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesEnableDnssecCreateNsec3ErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NSEC_3_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NSEC_3_ERROR_COMPONENT_CODE_VALUES!r}"
    )
