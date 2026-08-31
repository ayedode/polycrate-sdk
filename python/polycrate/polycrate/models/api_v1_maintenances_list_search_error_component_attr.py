from typing import Literal

ApiV1MaintenancesListSearchErrorComponentAttr = Literal["search"]

API_V1_MAINTENANCES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_maintenances_list_search_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListSearchErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
