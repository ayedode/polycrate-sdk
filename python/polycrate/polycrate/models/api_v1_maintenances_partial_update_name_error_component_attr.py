from typing import Literal

ApiV1MaintenancesPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_maintenances_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateNameErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
