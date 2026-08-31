from typing import Literal

ApiV1MaintenanceWindowsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_MAINTENANCE_WINDOWS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_maintenance_windows_create_annotations_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
