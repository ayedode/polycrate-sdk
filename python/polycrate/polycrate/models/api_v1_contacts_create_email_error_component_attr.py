from typing import Literal

ApiV1ContactsCreateEmailErrorComponentAttr = Literal["email"]

API_V1_CONTACTS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsCreateEmailErrorComponentAttr] = {
    "email",
}


def check_api_v1_contacts_create_email_error_component_attr(value: str) -> ApiV1ContactsCreateEmailErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
