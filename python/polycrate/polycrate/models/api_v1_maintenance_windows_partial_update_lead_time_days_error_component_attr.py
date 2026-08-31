from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponentAttr = Literal["lead_time_days"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_LEAD_TIME_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponentAttr
] = {
    "lead_time_days",
}


def check_api_v1_maintenance_windows_partial_update_lead_time_days_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_LEAD_TIME_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_LEAD_TIME_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
