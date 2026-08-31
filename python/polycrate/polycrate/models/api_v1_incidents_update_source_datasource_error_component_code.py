from typing import Literal

ApiV1IncidentsUpdateSourceDatasourceErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_INCIDENTS_UPDATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsUpdateSourceDatasourceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_incidents_update_source_datasource_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateSourceDatasourceErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_SOURCE_DATASOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
