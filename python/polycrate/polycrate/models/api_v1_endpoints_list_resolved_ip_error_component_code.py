from typing import Literal

ApiV1EndpointsListResolvedIpErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ENDPOINTS_LIST_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsListResolvedIpErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_endpoints_list_resolved_ip_error_component_code(
    value: str,
) -> ApiV1EndpointsListResolvedIpErrorComponentCode:
    if value in API_V1_ENDPOINTS_LIST_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_RESOLVED_IP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
