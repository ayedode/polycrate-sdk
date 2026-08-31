from typing import Literal

ApiV1ContactsArchiveCreateLastnameErrorComponentAttr = Literal["lastname"]

API_V1_CONTACTS_ARCHIVE_CREATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsArchiveCreateLastnameErrorComponentAttr
] = {
    "lastname",
}


def check_api_v1_contacts_archive_create_lastname_error_component_attr(
    value: str,
) -> ApiV1ContactsArchiveCreateLastnameErrorComponentAttr:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
