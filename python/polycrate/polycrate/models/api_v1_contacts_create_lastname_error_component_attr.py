from typing import Literal

ApiV1ContactsCreateLastnameErrorComponentAttr = Literal["lastname"]

API_V1_CONTACTS_CREATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsCreateLastnameErrorComponentAttr] = {
    "lastname",
}


def check_api_v1_contacts_create_lastname_error_component_attr(
    value: str,
) -> ApiV1ContactsCreateLastnameErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
