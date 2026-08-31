from typing import Literal

ApiV1MaintenancesPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_maintenances_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
