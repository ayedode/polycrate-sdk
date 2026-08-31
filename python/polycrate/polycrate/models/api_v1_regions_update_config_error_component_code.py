from typing import Literal

ApiV1RegionsUpdateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsUpdateConfigErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_regions_update_config_error_component_code(value: str) -> ApiV1RegionsUpdateConfigErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
