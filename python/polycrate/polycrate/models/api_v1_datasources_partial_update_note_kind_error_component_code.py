from typing import Literal

ApiV1DatasourcesPartialUpdateNoteKindErrorComponentCode = Literal[
    "blank", "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateNoteKindErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_datasources_partial_update_note_kind_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateNoteKindErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
