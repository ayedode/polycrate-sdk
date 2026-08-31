from typing import Literal

ApiV1MaintenancesListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_MAINTENANCES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesListStateNotErrorComponentAttr] = {
    "state_not",
}


def check_api_v1_maintenances_list_state_not_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListStateNotErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
