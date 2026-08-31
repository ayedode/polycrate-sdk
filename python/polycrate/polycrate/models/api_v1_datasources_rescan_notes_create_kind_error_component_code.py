from typing import Literal

ApiV1DatasourcesRescanNotesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_datasources_rescan_notes_create_kind_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateKindErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
