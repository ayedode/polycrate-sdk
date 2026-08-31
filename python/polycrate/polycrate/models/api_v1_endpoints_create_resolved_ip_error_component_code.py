from typing import Literal

ApiV1EndpointsCreateResolvedIpErrorComponentCode = Literal[
    "blank", "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ENDPOINTS_CREATE_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsCreateResolvedIpErrorComponentCode
] = {
    "blank",
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_endpoints_create_resolved_ip_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateResolvedIpErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
