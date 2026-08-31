from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_maintenance_windows_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
