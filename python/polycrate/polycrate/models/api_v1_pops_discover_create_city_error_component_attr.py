from typing import Literal

ApiV1PopsDiscoverCreateCityErrorComponentAttr = Literal["city"]

API_V1_POPS_DISCOVER_CREATE_CITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsDiscoverCreateCityErrorComponentAttr] = {
    "city",
}


def check_api_v1_pops_discover_create_city_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateCityErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_CITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_CITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
