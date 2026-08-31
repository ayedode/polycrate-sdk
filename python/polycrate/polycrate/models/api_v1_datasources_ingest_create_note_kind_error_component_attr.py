from typing import Literal

ApiV1DatasourcesIngestCreateNoteKindErrorComponentAttr = Literal["note_kind"]

API_V1_DATASOURCES_INGEST_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateNoteKindErrorComponentAttr
] = {
    "note_kind",
}


def check_api_v1_datasources_ingest_create_note_kind_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateNoteKindErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
