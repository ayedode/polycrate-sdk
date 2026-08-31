from typing import Literal

ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_partial_update_dnssec_enabled_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateDnssecEnabledErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
