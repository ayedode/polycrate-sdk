from typing import Literal

ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_rectify_create_dnssec_enabled_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
