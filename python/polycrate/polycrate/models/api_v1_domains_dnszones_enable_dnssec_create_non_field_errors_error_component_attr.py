from typing import Literal

ApiV1DomainsDnszonesEnableDnssecCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesEnableDnssecCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_domains_dnszones_enable_dnssec_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesEnableDnssecCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
