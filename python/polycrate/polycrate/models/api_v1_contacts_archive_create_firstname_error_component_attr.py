from typing import Literal

ApiV1ContactsArchiveCreateFirstnameErrorComponentAttr = Literal["firstname"]

API_V1_CONTACTS_ARCHIVE_CREATE_FIRSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsArchiveCreateFirstnameErrorComponentAttr
] = {
    "firstname",
}


def check_api_v1_contacts_archive_create_firstname_error_component_attr(
    value: str,
) -> ApiV1ContactsArchiveCreateFirstnameErrorComponentAttr:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_FIRSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_FIRSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
