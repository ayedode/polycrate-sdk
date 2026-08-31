from typing import Literal

ApiV1ContactsPartialUpdateEmailErrorComponentAttr = Literal["email"]

API_V1_CONTACTS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateEmailErrorComponentAttr
] = {
    "email",
}


def check_api_v1_contacts_partial_update_email_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateEmailErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
