from typing import Literal

ApiV1ContactsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CONTACTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_contacts_create_kind_error_component_attr(value: str) -> ApiV1ContactsCreateKindErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
