from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_maintenances_complete_early_create_criticality_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
