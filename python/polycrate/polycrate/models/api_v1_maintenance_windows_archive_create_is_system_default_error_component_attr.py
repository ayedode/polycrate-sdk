from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponentAttr = Literal["is_system_default"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponentAttr
] = {
    "is_system_default",
}


def check_api_v1_maintenance_windows_archive_create_is_system_default_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateIsSystemDefaultErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
