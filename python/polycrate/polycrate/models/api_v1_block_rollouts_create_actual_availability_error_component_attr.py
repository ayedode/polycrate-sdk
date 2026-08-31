from typing import Literal

ApiV1BlockRolloutsCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_BLOCK_ROLLOUTS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_block_rollouts_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
