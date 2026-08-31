from typing import Literal

ApiV1DatasourcesUpdateCreateIncidentsErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_UPDATE_CREATE_INCIDENTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateCreateIncidentsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_update_create_incidents_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateCreateIncidentsErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_CREATE_INCIDENTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_CREATE_INCIDENTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
