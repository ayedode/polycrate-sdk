from typing import Literal

ApiV1MaintenancesListSourceDatasourceErrorComponentAttr = Literal["source_datasource"]

API_V1_MAINTENANCES_LIST_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesListSourceDatasourceErrorComponentAttr
] = {
    "source_datasource",
}


def check_api_v1_maintenances_list_source_datasource_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListSourceDatasourceErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
