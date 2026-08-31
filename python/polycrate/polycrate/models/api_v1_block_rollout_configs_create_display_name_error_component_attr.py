from typing import Literal

ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_block_rollout_configs_create_display_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateDisplayNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
