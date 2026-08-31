from typing import Literal

ApiV1MaintenancesUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_MAINTENANCES_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_maintenances_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
