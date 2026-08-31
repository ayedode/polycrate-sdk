from typing import Literal

ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_CONDITION_INSTANCES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_condition_instances_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
