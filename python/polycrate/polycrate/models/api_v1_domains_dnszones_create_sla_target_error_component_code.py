from typing import Literal

ApiV1DomainsDnszonesCreateSlaTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_DOMAINS_DNSZONES_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesCreateSlaTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_domains_dnszones_create_sla_target_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesCreateSlaTargetErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
