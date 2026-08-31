from typing import Literal

ApiV1EndpointsPartialUpdateResolvedIpErrorComponentAttr = Literal["resolved_ip"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateResolvedIpErrorComponentAttr
] = {
    "resolved_ip",
}


def check_api_v1_endpoints_partial_update_resolved_ip_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateResolvedIpErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
