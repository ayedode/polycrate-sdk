from typing import Literal

ApiV1ContactsCreateContactRoleErrorComponentAttr = Literal["contact_role"]

API_V1_CONTACTS_CREATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsCreateContactRoleErrorComponentAttr
] = {
    "contact_role",
}


def check_api_v1_contacts_create_contact_role_error_component_attr(
    value: str,
) -> ApiV1ContactsCreateContactRoleErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
