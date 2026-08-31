from typing import Literal

ApiV1DatasourcesIngestCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DATASOURCES_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_datasources_ingest_create_criticality_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateCriticalityErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
