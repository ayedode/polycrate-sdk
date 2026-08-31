from typing import Literal

ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponentAttr = Literal["trigger_type"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TRIGGER_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponentAttr
] = {
    "trigger_type",
}


def check_api_v1_block_rollout_configs_update_trigger_type_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TRIGGER_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TRIGGER_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
