from typing import Literal

ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_maintenance_windows_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
