from typing import Literal

ApiV1ContactsPartialUpdateFirstnameErrorComponentAttr = Literal["firstname"]

API_V1_CONTACTS_PARTIAL_UPDATE_FIRSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateFirstnameErrorComponentAttr
] = {
    "firstname",
}


def check_api_v1_contacts_partial_update_firstname_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateFirstnameErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_FIRSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_FIRSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
