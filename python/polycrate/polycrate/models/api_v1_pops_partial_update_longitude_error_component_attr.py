from typing import Literal

ApiV1PopsPartialUpdateLongitudeErrorComponentAttr = Literal["longitude"]

API_V1_POPS_PARTIAL_UPDATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsPartialUpdateLongitudeErrorComponentAttr
] = {
    "longitude",
}


def check_api_v1_pops_partial_update_longitude_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateLongitudeErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
