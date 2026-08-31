from typing import Literal

ApiV1ContactsUpdatePhoneErrorComponentAttr = Literal["phone"]

API_V1_CONTACTS_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsUpdatePhoneErrorComponentAttr] = {
    "phone",
}


def check_api_v1_contacts_update_phone_error_component_attr(value: str) -> ApiV1ContactsUpdatePhoneErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
