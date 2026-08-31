from typing import Literal

ApiV1BlocksCreateConfigErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCreateConfigErrorComponentCode] = {
    "invalid",
}


def check_api_v1_blocks_create_config_error_component_code(value: str) -> ApiV1BlocksCreateConfigErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
