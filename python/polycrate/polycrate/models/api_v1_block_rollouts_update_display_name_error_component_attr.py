from typing import Literal

ApiV1BlockRolloutsUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_BLOCK_ROLLOUTS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_block_rollouts_update_display_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
