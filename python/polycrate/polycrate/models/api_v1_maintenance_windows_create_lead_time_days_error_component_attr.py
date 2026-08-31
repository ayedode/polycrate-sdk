from typing import Literal

ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponentAttr = Literal["lead_time_days"]

API_V1_MAINTENANCE_WINDOWS_CREATE_LEAD_TIME_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponentAttr
] = {
    "lead_time_days",
}


def check_api_v1_maintenance_windows_create_lead_time_days_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_CREATE_LEAD_TIME_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_CREATE_LEAD_TIME_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
