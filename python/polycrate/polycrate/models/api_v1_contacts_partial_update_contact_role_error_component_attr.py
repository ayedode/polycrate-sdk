from typing import Literal

ApiV1ContactsPartialUpdateContactRoleErrorComponentAttr = Literal["contact_role"]

API_V1_CONTACTS_PARTIAL_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateContactRoleErrorComponentAttr
] = {
    "contact_role",
}


def check_api_v1_contacts_partial_update_contact_role_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateContactRoleErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
