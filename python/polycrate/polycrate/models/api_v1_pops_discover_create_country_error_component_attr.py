from typing import Literal

ApiV1PopsDiscoverCreateCountryErrorComponentAttr = Literal["country"]

API_V1_POPS_DISCOVER_CREATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateCountryErrorComponentAttr
] = {
    "country",
}


def check_api_v1_pops_discover_create_country_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateCountryErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
