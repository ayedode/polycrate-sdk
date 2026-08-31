from typing import Literal

ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_block_rollouts_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
