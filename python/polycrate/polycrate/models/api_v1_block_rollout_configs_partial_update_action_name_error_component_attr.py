from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponentAttr = Literal["action_name"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_ACTION_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponentAttr
] = {
    "action_name",
}


def check_api_v1_block_rollout_configs_partial_update_action_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateActionNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_ACTION_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_ACTION_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
