from typing import Literal

ApiV1PopsPartialUpdateCountryErrorComponentAttr = Literal["country"]

API_V1_POPS_PARTIAL_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsPartialUpdateCountryErrorComponentAttr] = {
    "country",
}


def check_api_v1_pops_partial_update_country_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateCountryErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
