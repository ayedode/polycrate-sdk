from typing import Literal

ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_maintenances_archive_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
