from typing import Literal

ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_NSEC_3_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_update_dnssec_nsec_3_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesUpdateDnssecNsec3ErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_NSEC_3_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_NSEC_3_ERROR_COMPONENT_CODE_VALUES!r}"
    )
