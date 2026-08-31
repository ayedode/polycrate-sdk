from typing import Literal

ApiV1DomainsDnszonesCreateDefaultTtlErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DOMAINS_DNSZONES_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesCreateDefaultTtlErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_domains_dnszones_create_default_ttl_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesCreateDefaultTtlErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
