from typing import Literal

ApiV1EndpointsPartialUpdateResolvedIpErrorComponentCode = Literal[
    "blank", "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ENDPOINTS_PARTIAL_UPDATE_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateResolvedIpErrorComponentCode
] = {
    "blank",
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_endpoints_partial_update_resolved_ip_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateResolvedIpErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
