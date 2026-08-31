from typing import Literal

ApiV1ContactsUpdateContactRoleErrorComponentAttr = Literal["contact_role"]

API_V1_CONTACTS_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsUpdateContactRoleErrorComponentAttr
] = {
    "contact_role",
}


def check_api_v1_contacts_update_contact_role_error_component_attr(
    value: str,
) -> ApiV1ContactsUpdateContactRoleErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
