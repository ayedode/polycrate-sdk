from typing import Literal

ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_BLOCK_ROLLOUTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_block_rollouts_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
