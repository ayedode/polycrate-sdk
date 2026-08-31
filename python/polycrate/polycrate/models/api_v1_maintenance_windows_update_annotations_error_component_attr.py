from typing import Literal

ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_maintenance_windows_update_annotations_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
