from typing import Literal

ApiV1PopsUpdateLongitudeErrorComponentAttr = Literal["longitude"]

API_V1_POPS_UPDATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateLongitudeErrorComponentAttr] = {
    "longitude",
}


def check_api_v1_pops_update_longitude_error_component_attr(value: str) -> ApiV1PopsUpdateLongitudeErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
