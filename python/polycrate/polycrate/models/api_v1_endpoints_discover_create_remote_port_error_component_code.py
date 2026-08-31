from typing import Literal

ApiV1EndpointsDiscoverCreateRemotePortErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ENDPOINTS_DISCOVER_CREATE_REMOTE_PORT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateRemotePortErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_endpoints_discover_create_remote_port_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateRemotePortErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_REMOTE_PORT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_REMOTE_PORT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
