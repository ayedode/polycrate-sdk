from typing import Literal

ApiV1EndpointsPartialUpdateRemotePortErrorComponentAttr = Literal["remote_port"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateRemotePortErrorComponentAttr
] = {
    "remote_port",
}


def check_api_v1_endpoints_partial_update_remote_port_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateRemotePortErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
