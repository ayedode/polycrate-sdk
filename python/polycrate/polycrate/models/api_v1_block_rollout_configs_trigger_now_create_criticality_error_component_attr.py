from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollout_configs_trigger_now_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
