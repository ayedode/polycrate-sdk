from typing import Literal

ApiV1EndpointsDiscoverCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ENDPOINTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_endpoints_discover_create_criticality_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateCriticalityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
