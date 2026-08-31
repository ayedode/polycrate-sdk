from typing import Literal

ApiV1EndpointsCreateResolvedIpErrorComponentAttr = Literal["resolved_ip"]

API_V1_ENDPOINTS_CREATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateResolvedIpErrorComponentAttr
] = {
    "resolved_ip",
}


def check_api_v1_endpoints_create_resolved_ip_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateResolvedIpErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
