from typing import Literal

ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponentAttr = Literal["source_datasource"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponentAttr
] = {
    "source_datasource",
}


def check_api_v1_maintenances_archive_create_source_datasource_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
