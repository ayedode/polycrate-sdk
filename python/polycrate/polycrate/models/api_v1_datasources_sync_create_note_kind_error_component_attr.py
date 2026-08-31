from typing import Literal

ApiV1DatasourcesSyncCreateNoteKindErrorComponentAttr = Literal["note_kind"]

API_V1_DATASOURCES_SYNC_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateNoteKindErrorComponentAttr
] = {
    "note_kind",
}


def check_api_v1_datasources_sync_create_note_kind_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateNoteKindErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
