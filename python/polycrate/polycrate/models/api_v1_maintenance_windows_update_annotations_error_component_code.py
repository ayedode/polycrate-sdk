from typing import Literal

ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_maintenance_windows_update_annotations_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
