from typing import Literal

ApiV1MaintenancesListSourceDatasourceErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCES_LIST_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesListSourceDatasourceErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_maintenances_list_source_datasource_error_component_code(
    value: str,
) -> ApiV1MaintenancesListSourceDatasourceErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
