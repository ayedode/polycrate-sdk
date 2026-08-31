from typing import Literal

ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponentAttr = Literal["note_workspace_id"]

API_V1_DATASOURCES_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponentAttr
] = {
    "note_workspace_id",
}


def check_api_v1_datasources_create_note_workspace_id_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
