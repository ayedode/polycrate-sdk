from typing import Literal

ApiV1EndpointsUpdateRegionErrorComponentAttr = Literal["region"]

API_V1_ENDPOINTS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsUpdateRegionErrorComponentAttr] = {
    "region",
}


def check_api_v1_endpoints_update_region_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateRegionErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
