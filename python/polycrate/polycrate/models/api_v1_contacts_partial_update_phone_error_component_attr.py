from typing import Literal

ApiV1ContactsPartialUpdatePhoneErrorComponentAttr = Literal["phone"]

API_V1_CONTACTS_PARTIAL_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdatePhoneErrorComponentAttr
] = {
    "phone",
}


def check_api_v1_contacts_partial_update_phone_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdatePhoneErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
