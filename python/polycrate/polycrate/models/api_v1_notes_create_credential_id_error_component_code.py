from typing import Literal

ApiV1NotesCreateCredentialIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_NOTES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesCreateCredentialIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_notes_create_credential_id_error_component_code(
    value: str,
) -> ApiV1NotesCreateCredentialIdErrorComponentCode:
    if value in API_V1_NOTES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
