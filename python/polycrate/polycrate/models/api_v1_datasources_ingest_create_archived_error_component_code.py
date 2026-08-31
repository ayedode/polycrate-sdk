from typing import Literal

ApiV1DatasourcesIngestCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_INGEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesIngestCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_ingest_create_archived_error_component_code(
    value: str,
) -> ApiV1DatasourcesIngestCreateArchivedErrorComponentCode:
    if value in API_V1_DATASOURCES_INGEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
