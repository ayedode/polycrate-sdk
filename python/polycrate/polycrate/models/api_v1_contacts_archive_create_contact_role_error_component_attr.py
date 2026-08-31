from typing import Literal

ApiV1ContactsArchiveCreateContactRoleErrorComponentAttr = Literal["contact_role"]

API_V1_CONTACTS_ARCHIVE_CREATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsArchiveCreateContactRoleErrorComponentAttr
] = {
    "contact_role",
}


def check_api_v1_contacts_archive_create_contact_role_error_component_attr(
    value: str,
) -> ApiV1ContactsArchiveCreateContactRoleErrorComponentAttr:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_CONTACT_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
