from typing import Literal

ApiV1MaintenanceWindowsListKindErrorComponentAttr = Literal["kind"]

API_V1_MAINTENANCE_WINDOWS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_maintenance_windows_list_kind_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsListKindErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
