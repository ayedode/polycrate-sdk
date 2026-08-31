from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponentAttr = Literal["repair_task_meta"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponentAttr
] = {
    "repair_task_meta",
}


def check_api_v1_block_rollout_configs_trigger_now_create_repair_task_meta_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
