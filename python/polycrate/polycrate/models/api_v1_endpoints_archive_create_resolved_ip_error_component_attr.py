from typing import Literal

ApiV1EndpointsArchiveCreateResolvedIpErrorComponentAttr = Literal["resolved_ip"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateResolvedIpErrorComponentAttr
] = {
    "resolved_ip",
}


def check_api_v1_endpoints_archive_create_resolved_ip_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateResolvedIpErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_RESOLVED_IP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
