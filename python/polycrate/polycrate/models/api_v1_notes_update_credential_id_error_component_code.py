from typing import Literal

ApiV1NotesUpdateCredentialIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_NOTES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesUpdateCredentialIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_notes_update_credential_id_error_component_code(
    value: str,
) -> ApiV1NotesUpdateCredentialIdErrorComponentCode:
    if value in API_V1_NOTES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
