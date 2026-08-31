from typing import Literal

ApiV1MaintenanceWindowsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_maintenance_windows_update_name_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateNameErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
