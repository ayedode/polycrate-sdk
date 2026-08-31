from typing import Literal

ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_block_rollout_configs_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
