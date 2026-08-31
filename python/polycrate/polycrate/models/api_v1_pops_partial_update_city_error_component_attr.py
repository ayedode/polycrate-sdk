from typing import Literal

ApiV1PopsPartialUpdateCityErrorComponentAttr = Literal["city"]

API_V1_POPS_PARTIAL_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsPartialUpdateCityErrorComponentAttr] = {
    "city",
}


def check_api_v1_pops_partial_update_city_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateCityErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
