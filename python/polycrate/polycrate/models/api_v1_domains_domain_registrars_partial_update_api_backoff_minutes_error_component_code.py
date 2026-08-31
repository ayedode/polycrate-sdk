from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_domains_domain_registrars_partial_update_api_backoff_minutes_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
