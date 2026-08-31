from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateStartErrorComponentAttr = Literal["start"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_START_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateStartErrorComponentAttr
] = {
    "start",
}


def check_api_v1_maintenances_complete_early_create_start_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateStartErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_START_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_START_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
