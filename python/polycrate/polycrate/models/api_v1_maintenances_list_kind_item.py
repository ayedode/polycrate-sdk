from typing import Literal

ApiV1MaintenancesListKindItem = Literal["generic"]

API_V1_MAINTENANCES_LIST_KIND_ITEM_VALUES: set[ApiV1MaintenancesListKindItem] = {
    "generic",
}


def check_api_v1_maintenances_list_kind_item(value: str) -> ApiV1MaintenancesListKindItem:
    if value in API_V1_MAINTENANCES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_KIND_ITEM_VALUES!r}")
