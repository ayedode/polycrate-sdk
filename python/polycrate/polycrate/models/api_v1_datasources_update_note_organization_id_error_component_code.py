from typing import Literal

ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DATASOURCES_UPDATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_datasources_update_note_organization_id_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
