from typing import Literal

ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponentAttr = Literal["enqueue_reason"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponentAttr
] = {
    "enqueue_reason",
}


def check_api_v1_block_rollout_configs_create_enqueue_reason_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateEnqueueReasonErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
