from typing import Literal

ApiV1ContactsArchiveCreateEmailErrorComponentAttr = Literal["email"]

API_V1_CONTACTS_ARCHIVE_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsArchiveCreateEmailErrorComponentAttr
] = {
    "email",
}


def check_api_v1_contacts_archive_create_email_error_component_attr(
    value: str,
) -> ApiV1ContactsArchiveCreateEmailErrorComponentAttr:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
