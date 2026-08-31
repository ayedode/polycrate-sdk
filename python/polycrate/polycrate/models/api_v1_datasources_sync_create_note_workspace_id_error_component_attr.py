from typing import Literal

ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponentAttr = Literal["note_workspace_id"]

API_V1_DATASOURCES_SYNC_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponentAttr
] = {
    "note_workspace_id",
}


def check_api_v1_datasources_sync_create_note_workspace_id_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_NOTE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
