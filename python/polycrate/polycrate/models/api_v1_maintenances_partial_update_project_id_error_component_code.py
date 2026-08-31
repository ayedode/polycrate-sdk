from typing import Literal

ApiV1MaintenancesPartialUpdateProjectIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateProjectIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_maintenances_partial_update_project_id_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateProjectIdErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
