from typing import Literal

ApiV1EndpointsDiscoverCreateRegionErrorComponentAttr = Literal["region"]

API_V1_ENDPOINTS_DISCOVER_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateRegionErrorComponentAttr
] = {
    "region",
}


def check_api_v1_endpoints_discover_create_region_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateRegionErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
