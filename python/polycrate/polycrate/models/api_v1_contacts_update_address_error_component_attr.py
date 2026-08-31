from typing import Literal

ApiV1ContactsUpdateAddressErrorComponentAttr = Literal["address"]

API_V1_CONTACTS_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsUpdateAddressErrorComponentAttr] = {
    "address",
}


def check_api_v1_contacts_update_address_error_component_attr(
    value: str,
) -> ApiV1ContactsUpdateAddressErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
