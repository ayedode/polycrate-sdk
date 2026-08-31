from typing import Literal

ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_maintenances_archive_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
