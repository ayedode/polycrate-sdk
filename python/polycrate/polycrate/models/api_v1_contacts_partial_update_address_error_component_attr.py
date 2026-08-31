from typing import Literal

ApiV1ContactsPartialUpdateAddressErrorComponentAttr = Literal["address"]

API_V1_CONTACTS_PARTIAL_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateAddressErrorComponentAttr
] = {
    "address",
}


def check_api_v1_contacts_partial_update_address_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateAddressErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
