from typing import Literal

ApiV1MaintenancesCreateEndErrorComponentAttr = Literal["end"]

API_V1_MAINTENANCES_CREATE_END_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesCreateEndErrorComponentAttr] = {
    "end",
}


def check_api_v1_maintenances_create_end_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateEndErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_END_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_END_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
