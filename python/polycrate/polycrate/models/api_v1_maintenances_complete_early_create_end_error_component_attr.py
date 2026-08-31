from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateEndErrorComponentAttr = Literal["end"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateEndErrorComponentAttr
] = {
    "end",
}


def check_api_v1_maintenances_complete_early_create_end_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateEndErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_END_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
