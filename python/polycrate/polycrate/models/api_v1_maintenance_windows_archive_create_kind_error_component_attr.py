from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_maintenance_windows_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
