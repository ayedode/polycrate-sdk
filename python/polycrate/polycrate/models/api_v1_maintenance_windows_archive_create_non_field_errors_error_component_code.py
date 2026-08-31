from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenance_windows_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
