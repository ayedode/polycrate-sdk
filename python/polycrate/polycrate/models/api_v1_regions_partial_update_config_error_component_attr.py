from typing import Literal

ApiV1RegionsPartialUpdateConfigErrorComponentAttr = Literal["config"]

API_V1_REGIONS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_regions_partial_update_config_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateConfigErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
