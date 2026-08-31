from typing import Literal

ApiV1DatasourcesArchiveCreateNoteKindErrorComponentAttr = Literal["note_kind"]

API_V1_DATASOURCES_ARCHIVE_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateNoteKindErrorComponentAttr
] = {
    "note_kind",
}


def check_api_v1_datasources_archive_create_note_kind_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateNoteKindErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_NOTE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
