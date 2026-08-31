from typing import Literal

ApiV1BlocksCreateConfigErrorComponentAttr = Literal["config"]

API_V1_BLOCKS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateConfigErrorComponentAttr] = {
    "config",
}


def check_api_v1_blocks_create_config_error_component_attr(value: str) -> ApiV1BlocksCreateConfigErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
