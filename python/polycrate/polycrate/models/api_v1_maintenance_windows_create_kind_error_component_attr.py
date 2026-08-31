from typing import Literal

ApiV1MaintenanceWindowsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_MAINTENANCE_WINDOWS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_maintenance_windows_create_kind_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateKindErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
