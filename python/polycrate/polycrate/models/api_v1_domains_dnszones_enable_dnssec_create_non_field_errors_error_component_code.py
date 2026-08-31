from typing import Literal

ApiV1DomainsDnszonesEnableDnssecCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesEnableDnssecCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_enable_dnssec_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesEnableDnssecCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
