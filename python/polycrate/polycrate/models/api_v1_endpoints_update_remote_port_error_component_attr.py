from typing import Literal

ApiV1EndpointsUpdateRemotePortErrorComponentAttr = Literal["remote_port"]

API_V1_ENDPOINTS_UPDATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateRemotePortErrorComponentAttr
] = {
    "remote_port",
}


def check_api_v1_endpoints_update_remote_port_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateRemotePortErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
