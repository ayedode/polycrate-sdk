from typing import Literal

ApiV1BlocksPartialUpdateConfigErrorComponentAttr = Literal["config"]

API_V1_BLOCKS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_blocks_partial_update_config_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateConfigErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
