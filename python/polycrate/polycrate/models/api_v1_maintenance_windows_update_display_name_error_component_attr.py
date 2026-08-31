from typing import Literal

ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_maintenance_windows_update_display_name_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
