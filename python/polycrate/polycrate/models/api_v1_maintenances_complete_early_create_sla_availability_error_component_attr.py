from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_maintenances_complete_early_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
