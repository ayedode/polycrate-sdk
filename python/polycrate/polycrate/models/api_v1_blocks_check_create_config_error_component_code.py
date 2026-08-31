from typing import Literal

ApiV1BlocksCheckCreateConfigErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_CHECK_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCheckCreateConfigErrorComponentCode] = {
    "invalid",
}


def check_api_v1_blocks_check_create_config_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateConfigErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
