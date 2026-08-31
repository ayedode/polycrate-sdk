from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_block_rollout_configs_trigger_now_create_kind_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
