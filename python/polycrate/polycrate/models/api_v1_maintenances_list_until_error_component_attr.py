from typing import Literal

ApiV1MaintenancesListUntilErrorComponentAttr = Literal["until"]

API_V1_MAINTENANCES_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesListUntilErrorComponentAttr] = {
    "until",
}


def check_api_v1_maintenances_list_until_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListUntilErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
