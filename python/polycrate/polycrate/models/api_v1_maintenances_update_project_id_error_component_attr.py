from typing import Literal

ApiV1MaintenancesUpdateProjectIdErrorComponentAttr = Literal["project_id"]

API_V1_MAINTENANCES_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateProjectIdErrorComponentAttr
] = {
    "project_id",
}


def check_api_v1_maintenances_update_project_id_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateProjectIdErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
