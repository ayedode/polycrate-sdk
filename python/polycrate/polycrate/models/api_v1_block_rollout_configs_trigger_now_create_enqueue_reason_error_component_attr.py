from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponentAttr = Literal["enqueue_reason"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponentAttr
] = {
    "enqueue_reason",
}


def check_api_v1_block_rollout_configs_trigger_now_create_enqueue_reason_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
