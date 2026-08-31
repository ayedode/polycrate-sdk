from typing import Literal

ApiV1ContactsUpdateContactRoleErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONTACTS_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsUpdateContactRoleErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_contacts_update_contact_role_error_component_code(
    value: str,
) -> ApiV1ContactsUpdateContactRoleErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
