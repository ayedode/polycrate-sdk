from typing import Literal

ApiV1PopsDiscoverCreateLongitudeErrorComponentAttr = Literal["longitude"]

API_V1_POPS_DISCOVER_CREATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateLongitudeErrorComponentAttr
] = {
    "longitude",
}


def check_api_v1_pops_discover_create_longitude_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateLongitudeErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
