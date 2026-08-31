from typing import Literal

ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_maintenances_archive_create_source_datasource_error_component_code(
    value: str,
) -> ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponentCode:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
