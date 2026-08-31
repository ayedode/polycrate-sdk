from typing import Literal

ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_domains_dnszones_rectify_create_default_ttl_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
