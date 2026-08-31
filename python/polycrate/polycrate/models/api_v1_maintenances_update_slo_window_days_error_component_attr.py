from typing import Literal

ApiV1MaintenancesUpdateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_MAINTENANCES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_maintenances_update_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateSloWindowDaysErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
