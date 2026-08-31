from typing import Literal

ApiV1MaintenancesCreateStartErrorComponentAttr = Literal["start"]

API_V1_MAINTENANCES_CREATE_START_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesCreateStartErrorComponentAttr] = {
    "start",
}


def check_api_v1_maintenances_create_start_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateStartErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_START_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_START_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
