from typing import Literal

ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_block_rollouts_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
