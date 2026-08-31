from typing import Literal

ApiV1ContactsUpdateEmailErrorComponentAttr = Literal["email"]

API_V1_CONTACTS_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsUpdateEmailErrorComponentAttr] = {
    "email",
}


def check_api_v1_contacts_update_email_error_component_attr(value: str) -> ApiV1ContactsUpdateEmailErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
