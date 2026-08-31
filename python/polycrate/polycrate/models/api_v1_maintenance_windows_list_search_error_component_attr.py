from typing import Literal

ApiV1MaintenanceWindowsListSearchErrorComponentAttr = Literal["search"]

API_V1_MAINTENANCE_WINDOWS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_maintenance_windows_list_search_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsListSearchErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
