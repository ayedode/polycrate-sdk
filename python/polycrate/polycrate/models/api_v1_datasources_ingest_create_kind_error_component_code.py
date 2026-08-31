from typing import Literal

ApiV1DatasourcesIngestCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DATASOURCES_INGEST_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesIngestCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_datasources_ingest_create_kind_error_component_code(
    value: str,
) -> ApiV1DatasourcesIngestCreateKindErrorComponentCode:
    if value in API_V1_DATASOURCES_INGEST_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
