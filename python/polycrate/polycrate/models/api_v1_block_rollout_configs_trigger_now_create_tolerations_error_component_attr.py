from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_block_rollout_configs_trigger_now_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
