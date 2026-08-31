from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_block_rollout_configs_partial_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateSloTargetErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
