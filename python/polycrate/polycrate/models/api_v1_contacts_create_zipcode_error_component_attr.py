from typing import Literal

ApiV1ContactsCreateZipcodeErrorComponentAttr = Literal["zipcode"]

API_V1_CONTACTS_CREATE_ZIPCODE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsCreateZipcodeErrorComponentAttr] = {
    "zipcode",
}


def check_api_v1_contacts_create_zipcode_error_component_attr(
    value: str,
) -> ApiV1ContactsCreateZipcodeErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_ZIPCODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_ZIPCODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
