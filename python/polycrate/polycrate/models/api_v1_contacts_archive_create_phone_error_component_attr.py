from typing import Literal

ApiV1ContactsArchiveCreatePhoneErrorComponentAttr = Literal["phone"]

API_V1_CONTACTS_ARCHIVE_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsArchiveCreatePhoneErrorComponentAttr
] = {
    "phone",
}


def check_api_v1_contacts_archive_create_phone_error_component_attr(
    value: str,
) -> ApiV1ContactsArchiveCreatePhoneErrorComponentAttr:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
