from typing import Literal

ApiV1ContactsCreateCredentialIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_CONTACTS_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsCreateCredentialIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_contacts_create_credential_id_error_component_code(
    value: str,
) -> ApiV1ContactsCreateCredentialIdErrorComponentCode:
    if value in API_V1_CONTACTS_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
