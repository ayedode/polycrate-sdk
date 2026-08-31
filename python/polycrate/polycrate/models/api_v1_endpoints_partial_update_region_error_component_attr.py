from typing import Literal

ApiV1EndpointsPartialUpdateRegionErrorComponentAttr = Literal["region"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateRegionErrorComponentAttr
] = {
    "region",
}


def check_api_v1_endpoints_partial_update_region_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateRegionErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
