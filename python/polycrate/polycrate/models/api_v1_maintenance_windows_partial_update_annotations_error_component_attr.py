from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_maintenance_windows_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
