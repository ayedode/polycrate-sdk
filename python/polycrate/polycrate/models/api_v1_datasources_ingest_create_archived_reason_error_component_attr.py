from typing import Literal

ApiV1DatasourcesIngestCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_DATASOURCES_INGEST_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_datasources_ingest_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
