from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponentAttr = Literal["last_state"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponentAttr
] = {
    "last_state",
}


def check_api_v1_block_rollout_configs_trigger_now_create_last_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
