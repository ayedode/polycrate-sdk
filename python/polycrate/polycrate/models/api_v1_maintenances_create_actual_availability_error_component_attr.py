from typing import Literal

ApiV1MaintenancesCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_MAINTENANCES_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_maintenances_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
