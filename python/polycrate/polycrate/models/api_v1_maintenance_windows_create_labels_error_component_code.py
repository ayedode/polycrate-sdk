from typing import Literal

ApiV1MaintenanceWindowsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCE_WINDOWS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_maintenance_windows_create_labels_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsCreateLabelsErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
