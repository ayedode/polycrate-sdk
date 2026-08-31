from typing import Literal

ApiV1MaintenancesCreateNameErrorComponentAttr = Literal["name"]

API_V1_MAINTENANCES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1MaintenancesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_maintenances_create_name_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateNameErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
