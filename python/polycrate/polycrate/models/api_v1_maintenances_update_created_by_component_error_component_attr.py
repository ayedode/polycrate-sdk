from typing import Literal

ApiV1MaintenancesUpdateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_MAINTENANCES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_maintenances_update_created_by_component_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateCreatedByComponentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
