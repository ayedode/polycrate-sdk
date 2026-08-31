from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_maintenances_complete_early_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
