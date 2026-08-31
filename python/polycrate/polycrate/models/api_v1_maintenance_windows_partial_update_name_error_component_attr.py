from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_maintenance_windows_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
