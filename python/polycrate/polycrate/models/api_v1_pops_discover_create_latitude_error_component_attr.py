from typing import Literal

ApiV1PopsDiscoverCreateLatitudeErrorComponentAttr = Literal["latitude"]

API_V1_POPS_DISCOVER_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateLatitudeErrorComponentAttr
] = {
    "latitude",
}


def check_api_v1_pops_discover_create_latitude_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateLatitudeErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
