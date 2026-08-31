from typing import Literal

ApiV1MaintenanceWindowsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_MAINTENANCE_WINDOWS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_maintenance_windows_update_kind_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateKindErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
