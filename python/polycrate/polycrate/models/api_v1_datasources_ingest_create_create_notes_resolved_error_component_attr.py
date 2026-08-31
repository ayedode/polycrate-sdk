from typing import Literal

ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponentAttr = Literal["create_notes_resolved"]

API_V1_DATASOURCES_INGEST_CREATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponentAttr
] = {
    "create_notes_resolved",
}


def check_api_v1_datasources_ingest_create_create_notes_resolved_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
