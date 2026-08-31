from typing import Literal

ApiV1EndpointsListRemotePortErrorComponentCode = Literal["invalid", "max_value"]

API_V1_ENDPOINTS_LIST_REMOTE_PORT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsListRemotePortErrorComponentCode] = {
    "invalid",
    "max_value",
}


def check_api_v1_endpoints_list_remote_port_error_component_code(
    value: str,
) -> ApiV1EndpointsListRemotePortErrorComponentCode:
    if value in API_V1_ENDPOINTS_LIST_REMOTE_PORT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_REMOTE_PORT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
