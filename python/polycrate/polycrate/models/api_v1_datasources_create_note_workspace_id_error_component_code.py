from typing import Literal

ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DATASOURCES_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_datasources_create_note_workspace_id_error_component_code(
    value: str,
) -> ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponentCode:
    if value in API_V1_DATASOURCES_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
