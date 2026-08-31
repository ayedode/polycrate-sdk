from typing import Literal

ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponentAttr = Literal["block_name"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponentAttr
] = {
    "block_name",
}


def check_api_v1_block_rollout_configs_update_block_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateBlockNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
