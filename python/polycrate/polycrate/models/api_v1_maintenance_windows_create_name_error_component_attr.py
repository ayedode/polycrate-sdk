from typing import Literal

ApiV1MaintenanceWindowsCreateNameErrorComponentAttr = Literal["name"]

API_V1_MAINTENANCE_WINDOWS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_maintenance_windows_create_name_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateNameErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
