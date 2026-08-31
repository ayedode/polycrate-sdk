from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_maintenances_complete_early_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
