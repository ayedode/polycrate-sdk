from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_maintenances_complete_early_create_source_datasource_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
