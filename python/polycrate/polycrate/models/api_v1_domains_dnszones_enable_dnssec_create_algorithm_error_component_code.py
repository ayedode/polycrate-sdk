from typing import Literal

ApiV1DomainsDnszonesEnableDnssecCreateAlgorithmErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_ALGORITHM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesEnableDnssecCreateAlgorithmErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_dnszones_enable_dnssec_create_algorithm_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesEnableDnssecCreateAlgorithmErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_ALGORITHM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_ALGORITHM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
