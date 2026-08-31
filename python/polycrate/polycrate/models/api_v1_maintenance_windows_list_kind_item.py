from typing import Literal

ApiV1MaintenanceWindowsListKindItem = Literal["generic"]

API_V1_MAINTENANCE_WINDOWS_LIST_KIND_ITEM_VALUES: set[ApiV1MaintenanceWindowsListKindItem] = {
    "generic",
}


def check_api_v1_maintenance_windows_list_kind_item(value: str) -> ApiV1MaintenanceWindowsListKindItem:
    if value in API_V1_MAINTENANCE_WINDOWS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_LIST_KIND_ITEM_VALUES!r}")
