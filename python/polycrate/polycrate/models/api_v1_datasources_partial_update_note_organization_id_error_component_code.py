from typing import Literal

ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_datasources_partial_update_note_organization_id_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_NOTE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
