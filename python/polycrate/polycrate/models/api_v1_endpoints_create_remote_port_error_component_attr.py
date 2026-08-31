from typing import Literal

ApiV1EndpointsCreateRemotePortErrorComponentAttr = Literal["remote_port"]

API_V1_ENDPOINTS_CREATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateRemotePortErrorComponentAttr
] = {
    "remote_port",
}


def check_api_v1_endpoints_create_remote_port_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateRemotePortErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
