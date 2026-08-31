from typing import Literal

ApiV1EndpointsListRemotePortErrorComponentAttr = Literal["remote_port"]

API_V1_ENDPOINTS_LIST_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsListRemotePortErrorComponentAttr] = {
    "remote_port",
}


def check_api_v1_endpoints_list_remote_port_error_component_attr(
    value: str,
) -> ApiV1EndpointsListRemotePortErrorComponentAttr:
    if value in API_V1_ENDPOINTS_LIST_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_REMOTE_PORT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
