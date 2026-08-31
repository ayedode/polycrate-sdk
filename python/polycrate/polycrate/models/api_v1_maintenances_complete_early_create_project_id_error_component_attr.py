from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponentAttr = Literal["project_id"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponentAttr
] = {
    "project_id",
}


def check_api_v1_maintenances_complete_early_create_project_id_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
