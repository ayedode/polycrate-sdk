from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_sla_availability_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
