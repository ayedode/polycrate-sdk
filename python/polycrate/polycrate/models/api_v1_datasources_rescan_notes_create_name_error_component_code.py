from typing import Literal

ApiV1DatasourcesRescanNotesCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_datasources_rescan_notes_create_name_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateNameErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
