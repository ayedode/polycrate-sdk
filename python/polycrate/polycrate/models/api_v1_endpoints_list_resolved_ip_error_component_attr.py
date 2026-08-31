from typing import Literal

ApiV1EndpointsListResolvedIpErrorComponentAttr = Literal["resolved_ip"]

API_V1_ENDPOINTS_LIST_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsListResolvedIpErrorComponentAttr] = {
    "resolved_ip",
}


def check_api_v1_endpoints_list_resolved_ip_error_component_attr(
    value: str,
) -> ApiV1EndpointsListResolvedIpErrorComponentAttr:
    if value in API_V1_ENDPOINTS_LIST_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
