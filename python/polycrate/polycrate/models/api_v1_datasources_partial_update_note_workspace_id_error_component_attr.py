from typing import Literal

ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponentAttr = Literal["note_workspace_id"]

API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponentAttr
] = {
    "note_workspace_id",
}


def check_api_v1_datasources_partial_update_note_workspace_id_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
