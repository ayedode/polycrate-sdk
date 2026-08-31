from typing import Literal

ApiV1BlocksCheckCreateConfigErrorComponentAttr = Literal["config"]

API_V1_BLOCKS_CHECK_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCheckCreateConfigErrorComponentAttr] = {
    "config",
}


def check_api_v1_blocks_check_create_config_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateConfigErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
