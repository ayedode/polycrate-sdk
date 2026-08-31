from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateNameErrorComponentAttr = Literal["name"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_maintenances_complete_early_create_name_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateNameErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
