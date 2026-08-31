from typing import Literal

ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_block_rollout_configs_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
