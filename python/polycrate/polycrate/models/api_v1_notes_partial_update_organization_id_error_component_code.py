from typing import Literal

ApiV1NotesPartialUpdateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_NOTES_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesPartialUpdateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_notes_partial_update_organization_id_error_component_code(
    value: str,
) -> ApiV1NotesPartialUpdateOrganizationIdErrorComponentCode:
    if value in API_V1_NOTES_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
