from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_maintenance_windows_archive_create_description_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateDescriptionErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
