from typing import Literal

ApiV1MaintenancesListSinceErrorComponentAttr = Literal["since"]

API_V1_MAINTENANCES_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesListSinceErrorComponentAttr] = {
    "since",
}


def check_api_v1_maintenances_list_since_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListSinceErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
