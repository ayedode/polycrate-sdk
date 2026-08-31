from typing import Literal

ApiV1ContactsCreateAddressErrorComponentAttr = Literal["address"]

API_V1_CONTACTS_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsCreateAddressErrorComponentAttr] = {
    "address",
}


def check_api_v1_contacts_create_address_error_component_attr(
    value: str,
) -> ApiV1ContactsCreateAddressErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
