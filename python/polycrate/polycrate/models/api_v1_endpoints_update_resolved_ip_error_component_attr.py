from typing import Literal

ApiV1EndpointsUpdateResolvedIpErrorComponentAttr = Literal["resolved_ip"]

API_V1_ENDPOINTS_UPDATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateResolvedIpErrorComponentAttr
] = {
    "resolved_ip",
}


def check_api_v1_endpoints_update_resolved_ip_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateResolvedIpErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
