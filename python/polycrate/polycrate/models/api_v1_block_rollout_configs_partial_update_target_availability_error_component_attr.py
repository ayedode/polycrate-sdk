from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_block_rollout_configs_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
