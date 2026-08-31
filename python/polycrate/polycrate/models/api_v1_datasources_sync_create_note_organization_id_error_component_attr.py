from typing import Literal

ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponentAttr = Literal["note_organization_id"]

API_V1_DATASOURCES_SYNC_CREATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponentAttr
] = {
    "note_organization_id",
}


def check_api_v1_datasources_sync_create_note_organization_id_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
