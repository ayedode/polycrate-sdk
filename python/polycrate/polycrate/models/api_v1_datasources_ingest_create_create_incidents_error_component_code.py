from typing import Literal

ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_INGEST_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_ingest_create_create_incidents_error_component_code(
    value: str,
) -> ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponentCode:
    if value in API_V1_DATASOURCES_INGEST_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
