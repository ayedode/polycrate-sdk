from typing import Literal

ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_DOMAINS_DOMAINS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_domains_domains_create_sla_window_days_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
