from typing import Literal

ApiV1MaintenancesCreateProjectIdErrorComponentAttr = Literal["project_id"]

API_V1_MAINTENANCES_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateProjectIdErrorComponentAttr
] = {
    "project_id",
}


def check_api_v1_maintenances_create_project_id_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateProjectIdErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
