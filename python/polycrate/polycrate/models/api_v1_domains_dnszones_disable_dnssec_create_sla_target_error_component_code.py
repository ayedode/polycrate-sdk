from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_sla_target_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
