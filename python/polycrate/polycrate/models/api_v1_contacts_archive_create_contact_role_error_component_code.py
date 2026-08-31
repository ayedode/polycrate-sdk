from typing import Literal

ApiV1ContactsArchiveCreateContactRoleErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONTACTS_ARCHIVE_CREATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsArchiveCreateContactRoleErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_contacts_archive_create_contact_role_error_component_code(
    value: str,
) -> ApiV1ContactsArchiveCreateContactRoleErrorComponentCode:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
