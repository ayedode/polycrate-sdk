from typing import Literal

ApiV1ContactsPartialUpdateLastnameErrorComponentAttr = Literal["lastname"]

API_V1_CONTACTS_PARTIAL_UPDATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateLastnameErrorComponentAttr
] = {
    "lastname",
}


def check_api_v1_contacts_partial_update_lastname_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateLastnameErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_LASTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
