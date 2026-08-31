from typing import Literal

ApiV1PopsPartialUpdateLatitudeErrorComponentAttr = Literal["latitude"]

API_V1_POPS_PARTIAL_UPDATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsPartialUpdateLatitudeErrorComponentAttr
] = {
    "latitude",
}


def check_api_v1_pops_partial_update_latitude_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateLatitudeErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
