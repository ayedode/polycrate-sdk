from typing import Literal

ApiV1MaintenancesListPopErrorComponentAttr = Literal["pop"]

API_V1_MAINTENANCES_LIST_POP_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesListPopErrorComponentAttr] = {
    "pop",
}


def check_api_v1_maintenances_list_pop_error_component_attr(value: str) -> ApiV1MaintenancesListPopErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_POP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_POP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
