from typing import Literal

ApiV1ContactsPartialUpdateContactRoleErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONTACTS_PARTIAL_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsPartialUpdateContactRoleErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_contacts_partial_update_contact_role_error_component_code(
    value: str,
) -> ApiV1ContactsPartialUpdateContactRoleErrorComponentCode:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
