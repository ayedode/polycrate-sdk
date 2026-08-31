from typing import Literal

ApiV1MaintenanceWindowsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_maintenance_windows_update_labels_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateLabelsErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
