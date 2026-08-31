from typing import Literal

ApiV1ContactsCreatePhoneErrorComponentAttr = Literal["phone"]

API_V1_CONTACTS_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsCreatePhoneErrorComponentAttr] = {
    "phone",
}


def check_api_v1_contacts_create_phone_error_component_attr(value: str) -> ApiV1ContactsCreatePhoneErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
