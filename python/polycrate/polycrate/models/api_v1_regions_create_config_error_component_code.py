from typing import Literal

ApiV1RegionsCreateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsCreateConfigErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_regions_create_config_error_component_code(value: str) -> ApiV1RegionsCreateConfigErrorComponentCode:
    if value in API_V1_REGIONS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
