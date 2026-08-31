from typing import Literal

ApiV1MaintenancesPartialUpdateStartErrorComponentAttr = Literal["start"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_START_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateStartErrorComponentAttr
] = {
    "start",
}


def check_api_v1_maintenances_partial_update_start_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateStartErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_START_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_START_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
