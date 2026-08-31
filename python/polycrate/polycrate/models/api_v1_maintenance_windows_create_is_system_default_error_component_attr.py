from typing import Literal

ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponentAttr = Literal["is_system_default"]

API_V1_MAINTENANCE_WINDOWS_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponentAttr
] = {
    "is_system_default",
}


def check_api_v1_maintenance_windows_create_is_system_default_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
