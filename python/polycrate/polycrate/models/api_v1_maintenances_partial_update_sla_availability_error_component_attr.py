from typing import Literal

ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_maintenances_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
