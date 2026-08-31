from typing import Literal

ApiV1ContactsUpdateLastnameErrorComponentAttr = Literal["lastname"]

API_V1_CONTACTS_UPDATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsUpdateLastnameErrorComponentAttr] = {
    "lastname",
}


def check_api_v1_contacts_update_lastname_error_component_attr(
    value: str,
) -> ApiV1ContactsUpdateLastnameErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
