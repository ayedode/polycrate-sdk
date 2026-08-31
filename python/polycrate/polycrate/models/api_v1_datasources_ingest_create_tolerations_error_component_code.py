from typing import Literal

ApiV1DatasourcesIngestCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesIngestCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_ingest_create_tolerations_error_component_code(
    value: str,
) -> ApiV1DatasourcesIngestCreateTolerationsErrorComponentCode:
    if value in API_V1_DATASOURCES_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
